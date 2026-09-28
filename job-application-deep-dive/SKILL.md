---
name: job-application-deep-dive
description: On-demand deep-dive on one specific job opening a candidate wants to prioritize — researches the company/role, finds people to contact for a referral, drafts outreach, and tailors the candidate's résumé to the JD, flagging real gaps against the JD, verifying the résumé PDF actually parses cleanly, and scoring the final result before delivery. Use when asked to research a job posting in depth and prepare a full application package (not a quick résumé tweak — see tailor-resume for that alone).
license: MIT
---

# Job Application Deep-Dive

This skill is invoked on-demand, per opening, for a role the candidate has
decided they really want — so it goes deep instead of wide, and the
candidate reviews everything before anything is sent. It is not meant to
run over a bulk list of postings.

Before starting, establish the candidate's background (role/seniority,
tech stack, location, career stage) from the conversation, an attached
résumé, or by asking — everything below depends on knowing who you're
representing. If the candidate has a live/structured content source
(portfolio site, CV feed, etc.), fetch it fresh each time rather than
assuming its contents, since people update these.

This skill intentionally shares its tailoring logic, rendering template,
parseability check, and final scoring step with this repo's standalone
`tailor-resume` skill (Step 4 below), so the résumé output is identical
regardless of which skill produced it — if either changes, keep them in
sync.

## Input

The candidate will give a job posting URL (LinkedIn, Wellfound, company
careers page, etc.), sometimes with a note on why they like it. If they
haven't shared the URL yet, ask for it before doing anything else. If
they attach their own résumé file in the same message, treat that
attachment as authoritative for Step 4 (see below) instead of fetching
any other content source.

## Step 1: Understand the role and what the company actually wants

- Fetch the JD itself (or navigate to it with a browser if it needs
  JS/login — many job boards need a logged-in session). If the page's
  "how to apply" instructions use an obfuscated/encoded mailto (e.g. a
  Cloudflare email-protection hex string), decode it rather than
  reporting it as unreadable — Cloudflare's scheme is: first hex byte is
  the XOR key, XOR every following byte with it, and the ASCII result is
  the address.
- Fetch/search for the company: what they do, funding stage/investors
  (Crunchbase, TechCrunch, their own site), team size, recent news/
  launches, engineering blog or tech-stack posts if any. For a startup,
  check if they've posted on X/Twitter or LinkedIn recently about what
  they're building or hiring for.
- Synthesize: what does the JD's actual language suggest they value
  (e.g. heavy AI/LLM language vs. plain CRUD, "0-to-1" vs. "scale an
  existing system", explicit stack mentions)? Note anything that doesn't
  match the candidate's background so they go in aware, not blindsided —
  and say plainly in the deliverable which parts of the brief are
  verified fact vs. your own inference (see Delivery).

## Step 2: Find people to reach out to

- Search LinkedIn (the candidate's logged-in session, via whatever
  browser-automation tool is available) for employees at the company —
  prioritize: engineers/engineering managers on relevant teams,
  technical recruiters, and the hiring manager if identifiable from the
  JD or company org page. Search the company's LinkedIn people page with
  keyword filters ("engineer", "recruiter", "engineering manager")
  rather than relying on the unfiltered "people you may know" list,
  which is mostly noise. Note any 2nd-degree connections or shared
  alumni/background — those are the strongest referral asks.
- Also check the company's own team/about page, and search the web for
  founders/team members' X (Twitter), GitHub, or personal sites —
  useful for cold outreach when there's no LinkedIn connection path, and
  GitHub activity can reveal what they're actually working on.
- Produce a short ranked list (3-6 people) with: name, role, tenure/
  background if visible on their profile, why they're a good contact
  (team fit / referral path / responsiveness signal), and where found
  (LinkedIn URL, Twitter handle, etc). Do not fabricate contact details —
  if an email isn't publicly findable, say so rather than guessing one.

## Step 3: Draft outreach (draft only — never send)

First, work out how the role actually wants applications submitted (ATS
link, direct email, referral-only) — this shapes what "outreach" should
even be. If it's a direct-email application, the application email
itself is the most important draft in this whole skill, more important
than the LinkedIn notes below: write it in the candidate's own voice
(concise, direct, no filler, no recruiter-speak), anchored in one or two
concrete things they've actually built (not a generic "I'm a hard
worker" pitch), naming honestly any gap between their stack and the JD's
rather than dodging it — that reads as more human and more confident
than pretending the gap isn't there. Keep it short (150-220 words); a
wall of text undoes the human effect.

For each LinkedIn contact from Step 2, draft a short, specific,
non-generic message — referencing something real (their work,
background, the team, the JD) rather than a template-feeling pitch.
Produce both forms so the candidate can pick per-contact:
- A LinkedIn connection-request note (under ~300 characters — it gets
  read in seconds, so don't overwrite it) + a longer follow-up DM (if
  the note gets accepted)
- A cold email (if a work email is plausible/findable, or the candidate
  wants to send from their own address)

Frame these LinkedIn notes as secondary/optional next steps after the
application itself, not the main event, when the role has a direct
application path. Never claim a connection, referral relationship, or
shared background that isn't true. These are drafts for the candidate to
edit and send themself — do not attempt to actually send emails or
LinkedIn messages on their behalf, and do not send anything even if told
to "send it" unless a mail/messaging tool is actually connected in the
session and the candidate has confirmed that specific send.

## Step 4: Tailor the résumé

### Hard rule

Only reorder, select, and rephrase content that already exists in the
candidate's own material. Never add a skill, metric, employer, project,
or claim that isn't already true and already present in the source
content. If the JD needs something the candidate's content doesn't have,
leave it out of the résumé — but surface it explicitly (see "Flag real
gaps" below) rather than silently omitting it. (Where honesty about a
real gap is worth surfacing rather than hiding, it can also go in the
Step 3 application email, not just the résumé gap note.)

### Get the candidate's content

In priority order:
1. **An attached résumé file**, if given with this request — treat it
   as authoritative for both content and structure. Extract its text
   as-is; don't pull in a project, skill, or role that isn't already
   present in it, and don't restructure its section order without being
   asked.
2. **A structured content source** the candidate maintains (e.g. a
   personal-site JSON/CV feed with a superset of roles/projects/skills,
   possibly with multiple curated "lanes"/variants for different role
   types). Try fetching it; treat it as unreachable if it 404s, times
   out, or doesn't have the expected shape. If it has multiple lanes,
   pick whichever lane's headline/objective/curated projects best fit
   the JD's role title and domain language, and ask the candidate if the
   fit is genuinely ambiguous.
3. **A plain-text description of their background**, as the last
   resort, given directly in the conversation.

### Extract what the JD actually weights

Pull keywords/phrases from three specific places — this is what actually
correlates with clearing initial screening, not just skimming the whole
JD for buzzwords:
1. **The opening paragraph / responsibilities intro** — signals what the
   employer values most about the role.
2. **The qualifications/requirements section** — the actual gate
   criteria. Separate into **must-haves** (explicit required
   years/tech/degree, anything phrased as required) vs **nice-to-haves**
   (preferred/bonus/plus).
3. **Terms that repeat multiple times across the posting** — repetition
   signals weight, not just presence.

This is a guide to phrasing and priority for the next step, not a bag of
words to stuff in anywhere.

### Flag real gaps before assembling anything

Compare the must-haves and heavily-repeated terms above against the
candidate's actual available content. For anything genuinely missing or
weak (not just phrased differently — actually absent), note it now for
the Delivery summary. Don't compensate for a real gap by stretching a
bullet to imply something untrue — name the gap plainly instead; it's
more useful to the candidate than a résumé that quietly hopes they won't
be asked about it.

### Assemble the tailored content

Apply all five of these together on the eligible content from whichever
source you used above — they're the actual research findings behind
good résumé-tailoring, not just style notes:

- **Select and reorder** projects and skill groups by relevance to the
  JD's extracted terms — surface what matters most for this role first;
  a project with no relevance can drop lower or be cut if space is tight
  (résumé stays one page, matching the template below). For a new-grad/
  early-career profile, 2-3 strong, relevant projects shown in depth
  beat a longer list shown thinly — cut breadth for depth when space is
  tight.
- **Use the JD's exact words, not your synonyms.** When an existing
  bullet already describes the same real fact the JD asks for, switch
  the phrasing to the JD's own term instead of a synonym — e.g. if the
  JD says "CI/CD pipelines" and the existing bullet says "automated
  deployment" for the same actual work, use "CI/CD pipelines." Only do
  this when the underlying fact genuinely matches — otherwise it's not
  translation, it's invention, which the hard rule forbids.
- **Weight by position.** Skim-readers and recruiters weight *where* a
  term sits, not just whether it appears — so the headline, the
  summary, and the first bullet or two of the most relevant entries are
  where the JD's top terms belong. Don't bury the most relevant match
  under three other bullets.
- **Quantify what you tailor toward.** A keyword sitting next to an
  existing number reads as evidence; a bare keyword reads as stuffing.
  When a bullet already has a metric, keep the JD-relevant phrasing
  attached to that same metric rather than as a separate, disconnected
  mention. Never invent a number to pair with a keyword that didn't
  already have one. Prefer an explicit Action + Result + Metric shape
  for bullets wherever the underlying fact supports it — this is the
  single most convergent signal for what actually earns a closer read.
- **Vary phrasing — don't repeat one keyword.** Don't reuse the
  identical JD phrase three or four times across the résumé just
  because it scored well; vary the wording bullet to bullet the way a
  person naturally would. Read the finished section over once: if a
  phrase sounds forced or repeated, it's overdone — soften or cut it.

Also lightly adjust the title line and summary to reflect the target
role's title/domain — a light edit in the candidate's existing voice,
not a rewrite from scratch. An identical résumé sent to every role,
generic buzzwords without specifics, and uniform robotic phrasing are
the actual "looks AI-generated" tells — avoiding those matters more than
raw keyword density.

Carry forward any of the candidate's standing résumé instructions from
what they've told you before (e.g. a section to omit, a specific wording
they've corrected). If you don't have that context this session, ask
rather than guessing wrong on a résumé they're about to send out.

## Step 5: Render the PDF

Use this repo's `tailor-resume` skill's template and renderer
(`tailor-resume/templates/resume_template.html` and
`tailor-resume/scripts/render_resume.py`) — reproduce that visual design
exactly, don't redesign it, and follow its render/fit-to-one-page/ATS
parseability-check procedure in full before moving on.

## Step 6: Score the final résumé before delivering

Run the tailored résumé and the JD from Step 1 through the
`resume-fit-check` skill's evaluation logic (invoke it, or apply its
steps directly here) to get the ATS-parseability read, keyword/match
score, human-scan-appeal score, and overall confidence number with
reasoning. This is the honest close-of-loop check on the résumé
specifically — separate from the company/outreach research in Steps 1-3
— so the candidate sees how the résumé itself is likely to perform, not
just that it was tailored.

## Delivery

Package the output as: a short company/role brief (Step 1, explicitly
flagging verified facts vs. your own inference), the ranked contact list
with draft LinkedIn messages (Step 2-3), the draft application email
front-and-center if the role uses direct-email applications (Step 3),
and the tailored one-page résumé PDF (Step 4-6). Include, plainly, any
real gaps flagged in Step 4's "Flag real gaps" pass and the Step 6
confidence score with its reasoning — not softened.

Always end with a plain summary of what's solid (verified facts, real
people found, decoded contact info) vs. speculative (inferred
priorities, unconfirmed emails, your read on tone/culture) so the
candidate knows what to double check before sending anything.

## Notes

- Never send an email or LinkedIn message on the candidate's behalf,
  even if told to "send it," unless a messaging tool is actually
  connected this session and they have confirmed that specific send in
  this conversation.
- This skill and `tailor-resume` intentionally render the exact same
  tailoring logic, template, parseability check, and scoring step so a
  résumé is equally reliable regardless of which skill produced it —
  keep them in sync if either changes.
