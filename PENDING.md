# PENDING — verify before publishing

This site was built from **public records only**. Nothing here was taken from the
school. Before the site goes live (or before you show it to the Manager), confirm
every row marked **MEDIUM** or **LOW**.

> **Most important:** the "प्रधानाचार्य का संदेश" (Principal's message) on
> `about.html` is **written by us**, not by Dr. Rampratap Rai. It must be replaced
> with his own words or approved by him before publishing. Do not let it go live
> as-is.

---

## 1. Facts used on the site

| # | Claim on the site | Source | Confidence | Action needed |
|---|---|---|---|---|
| 1 | Name: हरिद्वार राय इंटर कॉलेज | UDISE / iCBSE / CBSE-listing aggregators | HIGH | Confirm exact **Hindi spelling** from the gate signboard |
| 2 | Village: भभनियाँव | UDISE `Bhabhaniyav` | MEDIUM | Records show 4 variants: Bhabhaniyav, Bamhaniyav, Babhaniyaw, Bramhaniyav. **Signboard is the truth.** |
| 3 | Established 2000 | iCBSE, stackschools, schoolsworld, webconte | HIGH | — |
| 4 | Board: UP Board (UPMSP) | webconte (Board for class 10 & 12 = UPSBIHE) | HIGH | Say it out loud to the office |
| 5 | Classes 6 to 12 | UDISE | HIGH | — |
| 6 | Hindi medium | UDISE | HIGH | — |
| 7 | Co-educational | UDISE | HIGH | — |
| 8 | Private unaided, recognised | UDISE `5-Pvt. Unaided (Recognized)` | HIGH | — |
| 9 | UDISE code 09660510204 | stackschools (UDISE extract) | HIGH | Confirm from office printout |
| 10 | PIN 232106 | UDISE, iCBSE | HIGH | — |
| 11 | Phone **+91 94515 70855** | Google Maps business listing | MEDIUM | **Call it before you print anything.** If wrong, the whole pitch dies. |
| 12 | "1,700+ विद्यार्थी" | UDISE = 1,869; iCBSE = 1,740 | MEDIUM | Both figures exceed 1,700, so the claim is safe. Replace with the real number once confirmed. |
| 13 | Admission in classes **6, 9, 11** | Inferred from enrolment (63/45/71 vs 436/358/483/413) | MEDIUM | **Confirm with office.** If class 6 admission is closed, change the section. |
| 14 | Principal: डॉ. रामप्रताप राय | UDISE `School Head Master` | MEDIUM | Confirm designation (Principal vs Head Master) **and get permission to name him** |
| 15 | Physics & Chemistry labs | UDISE facilities extract | HIGH | Biology was blank in the record — that is why it is **not** claimed |
| 16 | Library, book bank, generator, digital board, drinking water, handwash, pucca boundary wall | UDISE facilities extract | HIGH | — |
| 17 | Office hours: Monday–Saturday | Assumed (typical) | LOW | Confirm actual timings; add them |
| 18 | Document list on admission page | Standard UP practice | LOW | Replace with the school's actual list |
| 19 | Map pin 25.385612, 83.37574 | Google Maps listing | MEDIUM | Open the map and confirm the pin is on the **school gate**, not the village |

## 2. Deliberately NOT stated (do not add without proof)

- **Teacher count** — sources say 17, 26 and "3 approx". All wrong-looking. Omitted.
- **Fee amounts** — unknown. The fee table says "कार्यालय से जानकारी लें".
- **Board results / pass percentage** — unknown. No numbers invented anywhere.
- **Playground** — not in the UDISE facilities extract. Not claimed.
- **Biology lab** — blank in the record. Not claimed.
- **Internet / computer lab for students** — UDISE says `Internet: False`, 1 laptop, 0 desktops. Nothing claimed.
- **Streams at class 11–12** (Science / Commerce / Arts) — not confirmed. The site only says "विषय/संकाय का चयन इसी समय होता है".
- **Google rating (4.1★, 82 reviews)** — real, but left off the site so it cannot go stale.
- **Any affiliation number** — UP Board schools do not publish a CBSE-style affiliation number. None invented.

## 3. Content the school must supply

| Item | Where it goes | Notes |
|---|---|---|
| Photos (6–10) | Gallery on `index.html` | Building, classrooms, labs, library, function. Replace the grey placeholder tiles. |
| Real logo | Header + favicon | Currently a placeholder "HR" monogram in `assets/img/logo.svg` |
| Fee structure | `admission.html` table | The single most requested piece of information |
| Board results | New section | Pass %, toppers, stream-wise |
| Streams offered at 11–12 | `admission.html` / `facilities.html` | Science / Commerce / Arts + subjects |
| Principal's message | `about.html` | **Must be his words** |
| Staff list | Optional new page | Names + designations |
| Holiday list / syllabus PDFs | Downloads | Optional |

## 4. Legal / ethical notes

- The site carries `<meta name="robots" content="noindex, nofollow">` and a
  `robots.txt` that blocks crawlers. **Keep both until the school approves.**
  An unofficial site ranking for their name would be a serious problem.
- The footer states in Hindi that this is a **proposal**. Keep that line until
  the school signs off, then remove it.
- Do not reuse the school's logo or photos in any other demo or portfolio
  without written permission.
- The contact form sends nothing to a server — it opens WhatsApp with a
  prefilled message. No data is stored anywhere.

## 5. After approval — small cleanups

1. Remove the `noindex` meta tag from all 6 pages.
2. Delete `robots.txt` (or replace with an allow-all file).
3. Remove the `proposal-note` block from the footer.
4. Add the real domain to `<link rel="canonical">` and `og:url`.
5. Register the domain **in the school's name**.
6. Add the site URL to their Google Business Profile (this is the actual win).
