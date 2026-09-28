---
name: tailor-resume
description: Tailors a candidate's résumé to a specific job description — pulls their real content, reorders/rephrases it truthfully (never inventing skills or metrics), renders a one-page PDF from the bundled template, flags real gaps against the JD, verifies the PDF parses cleanly for ATS, and scores the result. Use when asked to tailor, customize, or adapt a résumé for a specific job posting.
license: MIT
---

# Tailor Résumé

Produces one job-specific résumé PDF, built strictly from content the
candidate already has — never invented. This skill does no company
research, no networking/referral search, and no outreach drafting: JD in,
tailored PDF out, with an honest read on how well it'll actually do. It
shares its scoring logic with this repo's `resume-fit-check` skill (Step
7) — use that skill directly for its own scoring-only entry point.

## 0. Hard rule

Only reorder, select, and rephrase content that already exists in the
candidate's own material. Never add a skill, metric, employer, project,
or claim that isn't already true and already present in the source
content. If the JD needs something the candidate's content doesn't have,
leave it out of the résumé — but surface it explicitly in Step 3 rather
than silently omitting it; a hidden gap and a named gap cost the same on
paper, but a named one lets the candidate decide whether to apply anyway,
address it in a cover note, or skip the role.

## 1. Get the job description and extract what matters

Accept either a URL or pasted JD text.
- If it's a URL, fetch it and extract the actual JD text (title,
  responsibilities, qualifications/requirements, any "nice to have"
  section). If the page's own "how to apply" text uses an obfuscated
  mailto (e.g. a Cloudflare email-protection hex string), decode it
  rather than reporting it as unreadable — Cloudflare's scheme: the
  first hex byte is the XOR key, XOR every following byte with it, and
  the ASCII result is the address.
- If it's not a URL (or the fetch fails), treat the given text as the JD
  directly.

Pull keywords/phrases from three specific places — this is what actually
correlates with clearing initial screening, not just skimming the whole
JD for buzzwords:
1. **The opening paragraph** — signals what the employer values most
   about the role.
2. **The qualifications/requirements section** — the actual gate
   criteria. Separate these into **must-haves** (explicit required
   years/tech/degree, anything phrased as required) vs **nice-to-haves**
   (preferred/bonus/plus).
3. **Terms that repeat multiple times across the posting** — repetition
   signals weight, not just presence.

This list is a guide to phrasing and priority for Step 5 — not a bag of
words to stuff in anywhere.

## 2. Get the candidate's content

In priority order:
1. **An attached résumé file**, if one was given with this request —
   treat it as authoritative for both content and structure. Extract its
   text as-is; don't pull in a project, skill, or role that isn't already
   present in it, and don't restructure its section order without being
   asked.
2. **A structured content source**, if the candidate maintains one (e.g.
   a personal-site JSON feed, a notes doc, a markdown CV) with a superset
   of roles/projects/skills and possibly multiple curated "lanes"
   (e.g. a general-software-engineering variant vs. a data/ML-focused
   variant). If the candidate has told you about such a source in this
   conversation or a prior one, try it; treat it as unreachable if it
   404s, times out, or doesn't have the expected shape.
3. **A plain-text resume/profile description** given directly in the
   conversation, as the last resort.

If nothing is reachable or attached, stop and ask the candidate to attach
something — don't guess at their background.

## 3. Flag real gaps before assembling anything

Compare the must-haves and heavily-repeated terms from Step 1 against the
candidate's actual available content from Step 2. For anything genuinely
missing or weak (not just phrased differently — actually absent), note it
now so it can go in the Delivery summary. Don't let this turn into
padding the résumé to compensate — the fix for a real gap is telling the
candidate, not stretching a bullet to imply something untrue.

## 4. Decide the mode

**Mode A — tailor an attached résumé directly.** If a specific résumé
file was attached and the request was to tailor *that* one, treat it as
the authoritative source for structure and content selection. Extract
its existing text as-is. You may still consult a richer content source
(if reachable) for extra phrasing detail about a project/role already
mentioned in the attached file, but do not pull in a project, skill, or
role that isn't already present in the attached file — that would exceed
"tailor this," not fulfill it.

**Mode B — build from a full content source.** Otherwise, if a
structured content source with multiple curated "lanes"/variants exists,
compare the JD's role title, domain language, and requirements against
each lane's headline/objective and which projects/skills that lane
already curates, and pick whichever lane is the better fit. Don't
hardcode to a fixed set of lanes — read whatever the source actually
contains. If the fit is genuinely ambiguous, ask which lane rather than
guessing.

## 5. Assemble the tailored content

Working only from the chosen eligible projects/skills, apply all five of
these together — they're the actual research findings behind good
résumé-tailoring, not just style notes:

- **Select and reorder** projects and skill groups by relevance to the
  JD's extracted terms — surface what matters most for this role first;
  a project with no relevance can drop lower or be cut if space is tight
  (résumé stays one page). For an early-career profile, 2-3 strong,
  relevant projects shown in depth beat a longer list shown thinly — cut
  breadth for depth when space is tight.
- **Use the JD's exact words, not your synonyms.** When an existing
  bullet already describes the same real fact the JD asks for, switch
  the phrasing to the JD's own term instead of a synonym — e.g. if the
  JD says "CI/CD pipelines" and the existing bullet says "automated
  deployment" for the same actual work, use "CI/CD pipelines." Only do
  this when the underlying fact genuinely matches — otherwise it's not
  translation, it's invention, which rule 0 forbids.
- **Weight by position.** Skim-readers and recruiters weight *where* a
  term sits, not just whether it appears — so the headline, the
  summary/objective, and the first bullet or two of the most relevant
  entries are where the JD's top terms belong. Don't bury the most
  relevant match under three other bullets.
- **Quantify what you tailor toward.** A keyword sitting next to an
  existing number reads as evidence; a bare keyword reads as stuffing.
  When a bullet already has a metric, keep the JD-relevant phrasing
  attached to that same metric rather than as a separate, disconnected
  mention. Never invent a number to pair with a keyword that didn't
  already have one. Prefer an explicit Action + Result + Metric shape
  for bullets wherever the underlying fact supports it.
- **Vary phrasing — don't repeat one keyword.** Don't reuse the
  identical JD phrase three or four times across the résumé just because
  it scored well; vary the wording bullet to bullet the way a person
  naturally would. Re-read the finished section: if a phrase sounds
  forced or repeated, it's overdone — soften or cut it.

Also: lightly adjust the headline/objective to reflect the target role's
title/domain, staying consistent with the candidate's existing tone — a
light edit, not a rewrite from scratch. Sending an identical résumé to
every role, generic buzzwords without specifics, and uniform robotic
phrasing are the actual "looks AI-generated" tells — avoiding those
matters more than raw keyword density.

Carry forward any standing formatting instructions the candidate has
given before (e.g. a section to omit, a specific wording they've
corrected). If you don't have that context this session, ask rather than
guessing wrong on a résumé about to be sent out.

## 6. Render the PDF

This skill ships a fixed visual template — a serif, single-page,
black-and-blue layout: `templates/resume_template.html` (reference/
starting point) and `scripts/render_resume.py` (the actual renderer,
which takes a JSON payload — see the docstring at the top of that file
for the exact shape). Reproduce this template exactly; it is tuned and
should not be redesigned per request.

Fixed style rules, don't deviate:
- Serif font throughout (Liberation Serif / Times New Roman) — never
  switch to a sans-serif font for this template.
- Links are blue-and-underlined (`#1155cc`) by default — profile links,
  GitHub, portfolio, and project titles use this.
- Company names in the Experience section are the one exception:
  underlined but **black**, not blue (`.job-title a` overrides to
  `#000`) — still clickable, but visually secondary to the links that
  matter more (portfolio/projects). Only add a company link when the
  candidate gives you the actual URL or it's a real, well-known company
  site — never guess one.
- Project titles link to the specific case-study/live URL if one was
  given for that project; otherwise link to the candidate's portfolio
  homepage rather than guessing a slug.
- One page, always. No exceptions — if content is long, cut
  lower-relevance bullets/projects per Step 5's selection logic rather
  than shrinking to fit everything.

Steps:
1. Build the JSON payload per `scripts/render_resume.py`'s docstring and
   save it to a scratch file (e.g. `tailored.json`).
2. Run it: `python3 scripts/render_resume.py tailored.json out.pdf`
   (`pip install weasyprint` first if not already installed).
3. Check the page count:
   `python3 -c "from pypdf import PdfReader; print(len(PdfReader('out.pdf').pages))"`
   (`pip install pypdf` if needed).
4. **If more than 1 page**: find how much overflowed with `pdfplumber`
   (extract text per page, see how many chars/lines spilled to page 2),
   then tighten in this order, in small steps, re-rendering after each:
   `line-height` down in ~0.03 steps, then `font-size` down in ~0.1-0.15pt
   steps, then the `@page` margins down in ~0.05in steps, then
   `h2.section`/`hr.section`/`p.entry-head` margins down by 1px at a
   time. Cut a lower-relevance bullet or project (per Step 5's selection
   logic) before shrinking type past readability — don't sacrifice
   legibility to force a fit.
5. **If 1 page but with a large empty gap at the bottom** (more than
   roughly an inch of white space): do the reverse — nudge `font-size`
   and `line-height` up first, then section/entry margins, then `@page`
   margins, re-checking page count after each change so it doesn't tip
   to 2 pages.
6. Once it's one page, visually confirm it before delivering — don't
   trust char counts alone:
   ```bash
   pip install pdf2image -q  # if needed
   python3 -c "from pdf2image import convert_from_path; convert_from_path('out.pdf', dpi=150)[0].save('preview.png')"
   ```
   Then view the resulting PNG to check the font, link colors, and
   spacing actually look right.

### Verify the PDF actually parses cleanly (ATS check)

A good-looking PDF can still extract badly. Confirm it doesn't, rather
than assuming the single-column template is automatically safe:

```bash
pip install pdfplumber -q  # if needed
python3 -c "import pdfplumber; print(pdfplumber.open('out.pdf').pages[0].extract_text())"
```

Check the extracted text against the intended content: all section
headings present and in order (Summary, Experience, Projects, Core
Skills, Education), no dropped contact info or links, no scrambled line
order, no missing bullets. If something's missing or out of order,
that's a real parsing defect in this specific render, not a hypothetical
one — fix the underlying HTML/CSS (usually something unintentionally
producing an absolutely-positioned or multi-column element) and
re-render before moving on, rather than shipping a PDF that looks right
but doesn't extract right.

## 7. Score the final result before delivering

Run the tailored résumé and the same JD through the `resume-fit-check`
skill's evaluation logic (invoke it, or apply its steps directly here) to
get the ATS-parseability read, keyword/match score, human-scan-appeal
score, and overall confidence number with reasoning. This is the honest
close-of-loop check — don't skip it just because you just built the
résumé yourself; the point is an independent read against the same
criteria that should be applied to any résumé.

## 8. Deliver

Send the candidate the PDF. Alongside it, give a short plain-text note
(not another document) covering: which content source/lane was used (or
that the attached résumé was tailored directly), the JD terms/priorities
from Step 1 that the tailoring leaned into and where each landed
(headline/summary/which bullets), which projects/bullets got reordered
or reworded, any real gaps flagged in Step 3 (named plainly, not
softened), and the Step 7 confidence score with its reasoning — so the
candidate can sanity-check it before applying, not just trust it
blindly.

## Notes

- This skill does no company research, referral/networking outreach, or
  cover letters. If the request clearly needs that broader scope, say so
  rather than quietly expanding this skill's job — see this repo's
  `job-application-deep-dive` skill for that broader workflow.
- `templates/resume_template.html` and `scripts/render_resume.py` render
  the same visual design — keep them in sync if you customize one.
