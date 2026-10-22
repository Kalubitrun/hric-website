# Haridwar Rai Inter College — proposal website

A static, Hindi-first website prepared as a **proposal** for Haridwar Rai Inter
College, Bhabhaniyav (Kamalpur), Block Dhanapur, District Chandauli, U.P.

No frameworks, no build tools required to view it. Open `index.html` in a browser.

---

## Files

```
hric-website/
├── index.html          मुख्य पृष्ठ (home)
├── about.html          परिचय
├── admission.html      प्रवेश
├── facilities.html     सुविधाएँ
├── contact.html        संपर्क
├── en/index.html       short English summary
├── robots.txt          blocks search engines (remove after approval)
├── assets/
│   ├── css/style.css   all styling
│   ├── js/main.js      footer year + WhatsApp form
│   └── img/logo.svg    placeholder "HR" monogram
├── tools/build.py      regenerates all HTML (optional)
├── PENDING.md          ⚠ facts to verify before publishing
└── README.md           this file
```

## Before you show it to anyone

**Read `PENDING.md`.** It lists every claim on the site, where it came from, and
what still needs confirming. Three things matter most:

1. The **phone number** (+91 94515 70855) came from Google Maps — call it first.
2. The **Hindi spelling of भभनियाँव** — check the gate signboard.
3. The **Principal's message is written by us**, not by him. Replace or get it approved.

Nothing on the site invents a fee amount, a result, a stream, or a teacher count.

---

## Preview locally

```bash
cd hric-website
python3 -m http.server 8000
# open http://localhost:8000
```

Or simply double-click `index.html`.

## Publish a link to send to the school

### Option A — Netlify Drop (fastest, no account needed at first)

1. Go to <https://app.netlify.com/drop>
2. Drag the whole `hric-website` folder onto the page
3. You get a URL like `https://calm-fox-1234.netlify.app`
4. Rename it under *Site settings → Change site name* (e.g. `hric-proposal`)

### Option B — Cloudflare Pages

```bash
npx wrangler pages deploy . --project-name hric
```

### Option C — GitHub Pages

```bash
git init && git add . && git commit -m "proposal site"
# push to a repo, then Settings → Pages → deploy from branch (root)
```

All three are free. **Keep the `noindex` meta tag and `robots.txt`** until the
school approves — an unofficial site appearing in Google search for their name
would be a serious problem.

## Editing content

Two ways:

**Direct edit** — open the `.html` file and change the text. Everything is plain
HTML; no build step. The CSS handles layout automatically.

**Regenerate** — edit `tools/build.py` (all facts and copy are at the top and in
the page blocks), then:

```bash
python3 tools/build.py
```

⚠ If you edit the HTML by hand, do **not** run `build.py` afterwards — it will
overwrite your changes. Pick one workflow.

## Design notes

- Hindi-first. Headings in `Noto Serif Devanagari`, body in `Noto Sans Devanagari`,
  both with system fallbacks (Nirmala UI, Mangal), so text stays legible on a
  cheap Android even if the webfont never loads.
- Body text is 17–18px with 1.8 line-height and dark-grey (#4c5a68) secondary text
  — deliberately not the thin, low-contrast type that breaks on a 4G phone outdoors.
- Mobile-first: checked at 320px and 390px. The nav drops to its own row below the
  school name, buttons go full-width, key figures become a 2×2 grid, tables stay
  readable without horizontal scrolling, and every control is at least 44px tall.
- Line icons are inline SVG (no emoji, no icon font) so they look identical on
  every device.
- No backend. The enquiry form composes a WhatsApp message and opens it — nothing
  is stored, no email service, no server to maintain.
- Google Maps iframe is lazy-loaded, with an "open in Maps" fallback link.
- `prefers-reduced-motion` respected.

## Replacing the placeholders

| Placeholder | Replace with |
|---|---|
| Grey gallery tiles (6) | Real photos — building, classrooms, labs, library |
| `assets/img/logo.svg` | The school's real logo |
| Fee table "कार्यालय से जानकारी लें" | Actual fee amounts |
| Principal's message | His own words |

## After the school says yes

1. Remove `<meta name="robots" content="noindex, nofollow">` from all 6 pages.
2. Delete `robots.txt`.
3. Remove the `proposal-note` block from the footer.
4. Add the real domain to `<link rel="canonical">`.
5. Register the domain **in the school's name**, not yours.
6. Add the URL to their Google Business Profile — that is where the enquiries
   actually come from.
