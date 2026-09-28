# Job Search Skills

A small collection of [Claude Agent Skills](https://docs.claude.com/en/docs/agents-and-tools/agent-skills) for job hunting: tailoring a résumé to a specific posting, scoring how well a résumé will actually perform, and running a full research-and-outreach deep-dive on one opening.

Each skill lives in its own directory with a `SKILL.md` (YAML frontmatter + instructions), following [Anthropic's Agent Skills format](https://docs.claude.com/en/docs/agents-and-tools/agent-skills), plus any supporting scripts/templates it needs.

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

Drop any of these directories into a Claude Code / Claude Agent Skills
`skills/` directory (project-level `.claude/skills/` or your personal
skills directory) and Claude will pick them up automatically based on each
`SKILL.md`'s `description` field. See Anthropic's docs on
[Agent Skills](https://docs.claude.com/en/docs/agents-and-tools/agent-skills)
for how skill discovery and invocation works across Claude Code, the API,
and claude.ai.

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
