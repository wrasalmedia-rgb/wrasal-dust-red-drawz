#!/usr/bin/env python3
"""
Conformance test suite for schemas/asset.schema.json (draft 2020-12).

Produces the evidence required by SCHEMA-REVIEW-001 before the schema extension
can be ratified by the Human Creative Authority.

Run:  python3 schemas/tests/test-asset-schema.py
Deps: pyyaml, jsonschema

Exit code 0 = all tests behaved as expected (positive cases accepted,
negative cases rejected). Non-zero = a governance invariant is broken.
"""

import json
import os
import sys

try:
    import yaml
    from jsonschema import Draft202012Validator
except ImportError:
    sys.exit("SKIP: pyyaml / jsonschema not installed")

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SCHEMA_PATH = os.path.join(ROOT, "schemas", "asset.schema.json")
REGISTRY_PATH = os.path.join(ROOT, "production", "asset-registry.yaml")

schema = yaml.safe_load(open(SCHEMA_PATH))
validator = Draft202012Validator(schema)

results = []


def check(name, should_be_valid, instance):
    errors = sorted(validator.iter_errors(instance), key=lambda e: list(e.path))
    ok = (not errors) if should_be_valid else bool(errors)
    detail = ""
    if not ok:
        detail = ("expected VALID but got: " + errors[0].message) if should_be_valid else "expected INVALID but it was accepted"
    results.append((ok, name, detail))


def media(**kw):
    """Minimal valid media reference, overridable."""
    base = {
        "id": "img-test-001",
        "type": "image",
        "lineage": "original",
        "delivery_status": "GENERATED CANDIDATE",
        "storage_status": "recorded-only",
        "sha256": "a" * 64,
    }
    base.update(kw)
    return base


def asset(**kw):
    base = {
        "id": "test-asset-001",
        "category": "prop",
        "name": "Test Asset",
        "status": "proposed",
        "canon_status": "proposed",
        "approval_status": "pending-human-approval",
        "version": "0.2.0",
        "owner": "human-creative-authority",
        "dependencies": [],
    }
    base.update(kw)
    return base


# ---------------------------------------------------------------------------
# A. Backward compatibility — every existing registry entry must still validate
# ---------------------------------------------------------------------------
def section_a():
    registry = yaml.safe_load(open(REGISTRY_PATH))
    assets = registry.get("assets", [])
    bad = 0
    for a in assets:
        errs = list(validator.iter_errors(a))
        if errs:
            bad += 1
            results.append((False, "A/backward-compat: %s" % a.get("id"),
                            "; ".join(e.message for e in errs)[:200]))
    results.append((bad == 0,
                    "A1 backward compatibility: all %d existing asset-registry entries validate" % len(assets),
                    "%d entries failed" % bad if bad else ""))


# ---------------------------------------------------------------------------
# B. Negative cases — these MUST be rejected
# ---------------------------------------------------------------------------
def section_b():
    check("B1 APPROVED ASSET media without decision_id", False,
          asset(approved_media=[media(delivery_status="APPROVED ASSET",
                                      approved_by="human-creative-authority",
                                      approved_date="2026-10-17")]))

    check("B2 APPROVED ASSET approved by a non-human authority", False,
          asset(approved_media=[media(delivery_status="APPROVED ASSET",
                                      approved_by="production-architect",
                                      approved_date="2026-10-17",
                                      decision_id="decision-009")]))

    check("B3 media reference missing storage_status", False,
          asset(candidate_media=[{k: v for k, v in media().items() if k != "storage_status"}]))

    check("B4 media reference missing sha256", False,
          asset(candidate_media=[{k: v for k, v in media().items() if k != "sha256"}]))

    check("B5 malformed sha256 (not 64 hex chars)", False,
          asset(candidate_media=[media(sha256="not-a-hash")]))

    check("B6 preserved-retrievable but present=false", False,
          asset(candidate_media=[media(storage_status="preserved-retrievable", present=False)]))

    check("B7 preserved-retrievable but no path", False,
          asset(candidate_media=[media(storage_status="preserved-retrievable", present=True)]))

    check("B8 preservation-incident but present=true", False,
          asset(candidate_media=[media(storage_status="preservation-incident", present=True)]))

    check("B9 externally held media (path null) with no durable_uri", False,
          asset(candidate_media=[media(path=None, storage_status="recorded-only")]))

    check("B10 garment_spec_lock marked as a verification rule", False,
          asset(garment_spec_lock={"authority_type": "verification-rule",
                                   "decision_id": "decision-008"}))

    check("B11 calibrated_heuristic marked as a design constraint", False,
          asset(calibrated_heuristic={"authority_type": "design-constraint",
                                      "decision_id": "decision-010"}))

    check("B12 non-approved media carrying approved_by", False,
          asset(candidate_media=[media(delivery_status="GENERATED CANDIDATE",
                                       approved_by="human-creative-authority")]))

    check("B13 unknown property inside a media reference", False,
          asset(candidate_media=[media(surprise_field="x")]))

    check("B14 garment_spec_lock missing decision_id", False,
          asset(garment_spec_lock={"authority_type": "design-constraint"}))

    # --- R-1: mandatory derivative provenance ---
    check("B15 derivative (lineage=derivative) with no derivative_of", False,
          asset(candidate_media=[media(lineage="derivative",
                                       transformation="convert -crop 1x1+0+0 +repage")]))

    check("B16 derivative with no transformation", False,
          asset(candidate_media=[media(lineage="derivative",
                                       derivative_of="img-master-001")]))

    check("B17 original (lineage=original) carrying a non-null derivative_of", False,
          asset(candidate_media=[media(lineage="original",
                                       derivative_of="img-master-001")]))

    check("B18 media reference missing lineage entirely", False,
          asset(candidate_media=[{k: v for k, v in media().items() if k != "lineage"}]))

    check("B19 derivative with an empty-string derivative_of", False,
          asset(candidate_media=[media(lineage="derivative",
                                       derivative_of="",
                                       transformation="convert -crop 1x1+0+0 +repage")]))

    check("B20 invalid lineage value", False,
          asset(candidate_media=[media(lineage="sort-of-derived")]))


# ---------------------------------------------------------------------------
# C. Positive cases — these MUST be accepted
# ---------------------------------------------------------------------------
def section_c():
    check("C1 APPROVED ASSET with full approval block AND preservation-incident "
          "(approval does not imply availability)", True,
          asset(approved_media=[media(delivery_status="APPROVED ASSET",
                                      storage_status="preservation-incident",
                                      present=False,
                                      decision_id="decision-009",
                                      approved_by="human-creative-authority",
                                      approved_date="2026-10-17")]))

    check("C2 candidate media with no approval block", True,
          asset(candidate_media=[media()]))

    check("C3 externally held media with path null + durable_uri", True,
          asset(candidate_media=[media(path=None, durable_uri="s3://bucket/key.png")]))

    check("C4 derivative carrying provenance (lineage + derivative_of + transformation)", True,
          asset(approved_media=[media(lineage="derivative",
                                      delivery_status="APPROVED ASSET",
                                      storage_status="preserved-retrievable",
                                      present=True,
                                      path="production/media/x.png",
                                      decision_id="decision-009",
                                      approved_by="human-creative-authority",
                                      approved_date="2026-10-17",
                                      derivative_of="img-master-001",
                                      transformation="convert -crop 1403x758+0+130 +repage")]))

    check("C5 design-constraint lock and verification-rule lock coexisting, each correctly typed", True,
          asset(garment_spec_lock={"authority_type": "design-constraint",
                                   "decision_id": "decision-008"},
                calibrated_heuristic={"authority_type": "verification-rule",
                                      "decision_id": "decision-010"}))

    check("C6 superseded media retaining prior checksums in sha256_history", True,
          asset(approved_media=[media(delivery_status="SUPERSEDED",
                                      storage_status="recorded-only",
                                      sha256_history=["b" * 64, "c" * 64])]))

    # --- R-1 ---
    check("C7 original asset explicitly declaring no lineage", True,
          asset(candidate_media=[media(lineage="original",
                                       derivative_of=None,
                                       transformation=None)]))

    check("C8 derivative naming both source and transformation", True,
          asset(candidate_media=[media(lineage="derivative",
                                       derivative_of="img-master-001",
                                       transformation="convert <master> -crop 1403x758+0+0 +repage <out>")]))


# ---------------------------------------------------------------------------
# D. Residual-risk probes — documented, not enforced
# ---------------------------------------------------------------------------
def section_d():
    ok = validator.is_valid(asset(
        garment_spec_lock={"authority_type": "design-constraint",
                           "decision_id": "decision-008",
                           "track_1_neutral_achromatic": "R/G <= 1.35"}))
    results.append((None,
                    "D1 RESIDUAL RISK: a verification rule smuggled into garment_spec_lock is "
                    "ACCEPTED (additionalProperties: true)" if ok else
                    "D1 RESIDUAL RISK: rejected",
                    "Mitigation: review-time, not schema-time. Keep the two blocks in separate "
                    "registers and diff them in SCHEMA-REVIEW-001."))

    ok = validator.is_valid(asset(approved_media=[media(
        delivery_status="APPROVED ASSET", storage_status="preserved-retrievable",
        present=True, path="production/media/x.png", decision_id="decision-009",
        approved_by="human-creative-authority", approved_date="2026-10-17",
        sha256="d" * 64, sha256_history=["e" * 64])]))
    results.append((None,
                    "D2 RESIDUAL RISK: an APPROVED ASSET whose sha256_history shows a changed "
                    "checksum is still ACCEPTED" if ok else
                    "D2 RESIDUAL RISK: rejected",
                    "Mitigation: sha256_history makes silent replacement VISIBLE on review; the "
                    "schema records it but cannot block it. Requires a human process control."))


# ---------------------------------------------------------------------------
# E. Versioning policy (R-6)
# ---------------------------------------------------------------------------
def section_e():
    hist = schema.get("version_history", [])
    required_keys = {"version", "date", "note", "compatibility", "tests"}
    malformed = [h.get("version", "<?>") for h in hist
                 if not required_keys.issubset(h)]
    results.append((not malformed,
                    "E1 version_history entries each record version, date, rationale, "
                    "compatibility assessment and tests (R-6)",
                    "malformed: %s" % malformed if malformed else "%d entries" % len(hist)))

    current = schema.get("schema_version", "").split("-")[0]
    results.append((any(h.get("version", "").startswith(current) or h.get("version") == current
                        for h in hist),
                    "E2 version_history contains an entry for the current schema_version "
                    "(%s)" % schema.get("schema_version"),
                    "no matching entry"))

    pol = schema.get("versioning_policy", {})
    results.append((bool(pol.get("patch")) and bool(pol.get("minor")) and bool(pol.get("major")),
                    "E3 semantic versioning policy declares patch / minor / major",
                    "missing definitions"))

    results.append(("asset" in json.dumps(pol.get("distinct_from_asset_versioning", "")).lower()
                    and "version" in pol.get("distinct_from_asset_versioning", "").lower(),
                    "E4 policy states that schema versioning is distinct from asset versioning",
                    "not stated"))

    results.append(("properties" in schema and "version" in schema["properties"],
                    "E5 assets carry their own 'version' field, independent of schema_version",
                    "no asset-level version property"))

    results.append((schema.get("schema_version") != schema.get("properties", {})
                    .get("version", {}).get("default"),
                    "E6 schema_version is not conflated with the asset version value",
                    "conflated"))


def main():
    section_a(); section_b(); section_c(); section_d(); section_e()
    width = max(len(n) for _, n, _ in results)
    failed = 0
    for ok, name, detail in results:
        tag = "PASS" if ok else ("INFO" if ok is None else "FAIL")
        if ok is False:
            failed += 1
        line = "[%s] %-*s" % (tag, width, name)
        print(line + ("  << " + detail if (detail and tag != "PASS") else ""))
    print()
    print("schema_version: %s" % schema.get("schema_version"))
    print("RESULT: %d/%d checks failed" % (failed, sum(1 for o, _, _ in results if o is not None)))
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
