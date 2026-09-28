# Contributing

Thanks for considering a contribution to this collection of job-hunting
agent skills.

## Ways to contribute

- **Fix or improve an existing skill** — clearer instructions, a bug in
  `scripts/render_resume.py`, a better-grounded scoring rule, etc.
- **Add a new skill** that fits the job-hunting workflow (e.g. interview
  prep, cover-letter drafting, salary-negotiation research).
- **Report an issue** — something a skill got wrong, an instruction that
  was ambiguous, or a step that didn't generalize well across agents.

## Ground rules for skill content

These skills are meant to work with *any* capable AI agent, not one
specific product:

- Write instructions in plain natural language. Don't reference a
  specific vendor's tool names (e.g. a particular product's fetch/browser
  tool) — describe the *capability* needed ("fetch the page", "run
  Python", "use a browser-automation tool if available") instead.
- Never hardcode a real person's personal details (name, contact info,
  employer, school, etc.) into a `SKILL.md` or template. Skills should
  read that information from whatever the user provides in each
  conversation.
- Keep the "never invent" rules intact. The résumé skills are built
  around a hard constraint: only reorder/rephrase content the candidate
  actually has, never fabricate a skill, metric, or claim. Any change to
  these skills must preserve that constraint.
- If you touch the résumé template or renderer, update **every** copy —
  `tailor-resume/templates/`, `tailor-resume/scripts/`,
  `job-application-deep-dive/templates/`, and
  `job-application-deep-dive/scripts/` are intentionally duplicated so
  each skill directory works standalone. Keep them identical.

## Adding a new skill

1. Create a new top-level directory named after the skill (kebab-case).
2. Add a `SKILL.md` with YAML frontmatter:
   ```yaml
   ---
   name: your-skill-name
   description: One or two sentences a triggering agent can match against — what the skill does and when to use it.
   license: MIT
   ---
   ```
3. Write the instructions as numbered steps, the way the existing skills
   are structured: inputs required, the actual procedure, how to produce
   the output, and what to flag to the user.
4. If the skill needs supporting files (scripts, templates), put them in
   `scripts/` and/or `templates/` inside that skill's own directory so it
   stays self-contained.
5. Add a row for it to the table in the root `README.md`.

## Testing your change

There's no CI here yet, so before opening a pull request:

- If you changed `scripts/render_resume.py`, run it against a sample JSON
  payload and confirm it produces a valid, one-page PDF
  (`python3 -m py_compile scripts/render_resume.py` at minimum; ideally
  also a real render).
- If you changed a `SKILL.md`, read it back top to bottom as if you were
  an agent seeing it cold — check that every step is actually
  followable without missing context.

## Pull requests

- Keep PRs focused on one skill or one clear change.
- Describe *what* changed and *why* in the PR description — no need to
  restate the obvious diff.
- Be ready to explain any new scoring weight, heuristic, or rule with the
  reasoning behind it; these skills are meant to be grounded in real
  research/behavior, not just intuition.
