# DELIVERY BOUNDARY 001 — Tested delivery methods did not produce a viewable image

**Record ID**: `DELIVERY-BOUNDARY-001`
**Date**: `2026-10-17`
**Established by**: Production Architect
**Reviewed by**: Human Creative Authority (`2026-10-17`) — **finding narrowed on review**
**Status**: **Delivery experiments SUSPENDED**
**Governs**: repetition of the delivery methods listed below

> **Standing instruction: the methods in §2 are not to be repeated.** They are settled negatives.
> This does **not** assert that no channel is possible — see §4. A qualitatively new method
> (one not reducible to the mechanisms in §2) would be a new decision, not a repetition.

---

## 1. Finding — stated narrowly

**The in-conversation delivery methods tested did not produce a viewable image for the Human
Creative Authority. Further delivery experiments are suspended.**

The PNG masters remain available through the external workspace, subject to retrieval by the human
reviewer.

**No defect in the underlying images is established or implied by this record.** Every artifact was
verified intact at the point of creation. The failure is at handoff, and even that is stated only for
the methods actually tried.

---

## 2. Evidence — what was observed

Facts only. No inference.

| # | Method | Size | Mechanism | Observed outcome |
|:--|:--|:--|:--|:--|
| 1 | `present_file` on PNG masters | 2.4–2.6 MB | native image | Not received |
| 2 | `present_file` on JPEG surrogates (1024 px) | 105 / 165 KB | native image | Not received |
| 3 | Live HTTP server, preview URL | full res | browser fetch | Reported blocked |
| 4 | Self-contained HTML, base64-embedded JPEGs | 376 KB | `<img src="data:...">` | Not received |
| 5 | Minimal HTML probe, base64-embedded 420 px | **11.8 KB** | `<img src="data:...">` | **Text received; image not rendered** |
| 6 | Inline SVG rectangle mosaic (Frame B) | 134 KB | SVG `<rect>` — **no `<img>`, no data URI** | **Text received; image not rendered** |

**Integrity facts established independently of delivery:**

- Channel 4's HTML contained **zero external references** — every `src` and `href` parsed as a `data:` URI.
- Its two embedded payloads were decoded and hashed: 127,796 B / `1402x1122` / `9c1c6429…ea026`, and 147,341 B / `1152x922` / `904a33e6…48e6f`. Both **byte-identical** to the registered derivatives.
- In channels 5 and 6, the authority received the surrounding text and reported no rendered image.

---

## 3. Interpretation — clearly separated from evidence

The following are **inferences** from §2, offered with stated confidence. They are not observations.

| Inference | Support | Confidence |
|:--|:--|:--|
| Size is not the operative variable in channels 5 and 6 | Channel 5 was ~1/32 the size of channel 4 and failed identically | **Well supported** |
| File format is not the operative variable | A raster (JPEG data URI) and a pure-vector text construct (inline SVG) both failed | **Well supported** |
| Path resolution is not the operative variable | Channel 4 had zero external references and intact payloads | **Well supported** |
| The receiving interface did not render graphics in channels 5 and 6 | Authority reported text but no picture in both | **Well supported** |

---

## 4. What this evidence does **NOT** establish

Recorded so that no future reader mistakes the scope of this finding.

1. **It does not establish that no in-conversation channel exists.** Six methods were tried. That is
   not an exhaustive enumeration of possible methods. The finding is about the methods tested.
2. **It does not establish that the receiving interface is incapable of rendering graphics.** It
   establishes that it did not render them in channels 5 and 6, under those conditions.
3. **It does not establish any defect, fault, or deficiency in Frame B, Frame C, or any derivative.**
   All artifacts verified intact. Asset quality is not in question here.
4. **It does not establish that the authority cannot see the images by other means.** Retrieval from
   the external workspace is unaffected and is the intended path.

---

## 5. Standing instruction — narrowed

- **Do not repeat** the six methods in §2, nor trivial variations of them (different sizes, different
  raster formats, re-encoded galleries, alternative embedding syntax). These are settled negatives;
  repeating them is repetition, not diligence.
- **Do not describe this record** as proving that in-conversation image delivery is impossible.
- **A qualitatively new method** — one not reducible to the mechanisms already tested — is a new
  decision requiring authority direction, not a resumption of suspended work.

---

## 6. Retrieval routes available to the authority

The masters are intact, checksum-verified, and reachable by routes that do not depend on
in-conversation rendering:

| Route | Detail |
|:--|:--|
| Workspace paths | `/home/user/wrasal-dust-red-drawz/verification/tests/TEST-DUST-C001-001/frame-b-shot-open-003-run-02.png`<br>`…/frame-c-shot-open-004-run-02.png` |
| Live HTTP server | Port 8000, serving the test directory (verified `HTTP 200` for both masters) |
| Notion metadata mirror | Identity and checksums only — **no pixels held there** |

Master checksums, re-verified `2026-10-17`:

- Frame B `run-02` — `img-red-drawz-001-open-003-run-02` — 1402×1122, 2,570,609 B — `ca0ac612e0d00be0ad55f7ff35d37d1d37b078b3097ed3f7c94cdaf5cbcd4cbf`
- Frame C `run-02` — `img-red-drawz-001-open-004-run-02` — 1152×922, 2,391,623 B — `e8bee9b5d10b69d8ffd78d1b41802738b0deb60a43660bf5b5dcdfa90a8434cb`

---

## 7. Disposition of the suspended artifacts

Per the media preservation policy, suspended artifacts are **retained, not deleted**. Their identity
and history survive so a future reader can see what was tried and why it stopped:

`frame-b-full.jpg`, `frame-c-full.jpg`, `frames-embedded.html`, `probe.jpg`, `probe.html`,
`svg-test.html`, `index.html` — all registered or recorded, all marked as review surrogates or
diagnostics, **none of them deliverables**.

---

## 8. Sign-off

| Field | Value |
|:--|:--|
| Experiments suspended | `2026-10-17` |
| Evidence gathered by | Production Architect |
| Finding narrowed on review by | Human Creative Authority, `2026-10-17` |
| Assets remain | Unapproved — pending human visual assessment |
| Schema | **Unchanged.** Existing permitted vocabulary used; no enum widened. |
| Resumption condition | Authority direction, on a qualitatively new method (§5) |
