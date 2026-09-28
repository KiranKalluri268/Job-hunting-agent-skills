# Agent Skills

A small collection of portable AI agent skills for job hunting: tailoring a résumé to a specific posting, scoring how well a résumé will actually perform, and running a full research-and-outreach deep-dive on one opening.

Each skill lives in its own directory with a `SKILL.md` — a plain-Markdown file with a short YAML frontmatter block (`name` + `description`) followed by step-by-step natural-language instructions — plus any supporting scripts/templates it needs. This is a common, framework-agnostic convention for packaging reusable agent instructions: no special runtime, SDK, or vendor lock-in required. Any AI agent or assistant that can read a Markdown file, follow instructions, and call tools (web fetch, shell/Python execution, file I/O) can use these as-is.

## Skills

| Skill | What it does |
|---|---|
| [`resume-fit-check`](./resume-fit-check) | Diagnoses (doesn't rewrite) how well a résumé will pass ATS parsing and a human recruiter's ~7-10 second scan for a given job description. Produces a parseability read, keyword/match score, human-scan-appeal score, an overall confidence number, and a prioritized fix list. |
| [`tailor-resume`](./tailor-resume) | Tailors a candidate's résumé to a specific job description — reorders and rephrases only content the candidate already has (never invents anything), renders a one-page PDF from the bundled template, verifies it parses cleanly, and scores the result. |
| [`job-application-deep-dive`](./job-application-deep-dive) | The full workflow for one opening a candidate really wants: company/role research, finding people to contact for a referral, drafting (never sending) outreach, and tailoring the résumé — reusing `tailor-resume`'s template and `resume-fit-check`'s scoring. |

`tailor-resume` and `job-application-deep-dive` intentionally share the same
tailoring logic, résumé template, and scoring step, so the résumé output is
identical no matter which one produced it.

## Using these skills

These are not tied to any one product or SDK. Two ways to use them:

- **Skill-aware agents/tools**: some agent runtimes auto-discover skills by
  scanning a directory of `SKILL.md` files and matching each one's
  `description` against the current task. If your tool works this way,
  point it at (or drop these directories into) wherever it looks for
  skills.
- **Any other agent, assistant, or workflow**: just hand it the relevant
  `SKILL.md` as context/instructions (paste it in, attach it, or have the
  agent read the file) alongside the job description and résumé. The
  instructions are self-contained plain-language steps with no
  vendor-specific syntax, so any capable model/agent that can fetch a URL,
  run Python, and read/write files can follow them directly.

These skills are written generically — they ask for (or expect an
attached) résumé/job description each time rather than hardcoding any one
person's details. `tailor-resume`'s renderer (`scripts/render_resume.py`)
takes a JSON payload described in its own docstring, so you can swap in
your own content source (a personal-site CV feed, a plain file, etc.)
without changing the skill's logic.

## Requirements

The résumé-rendering and PDF-checking steps shell out to a few Python
packages:

```bash
pip install weasyprint pypdf pdfplumber pdf2image
```

(`pdf2image` also requires `poppler` on your system PATH for page preview
rendering.)

## License

MIT — see [LICENSE](./LICENSE).
