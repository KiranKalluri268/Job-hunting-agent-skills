#!/usr/bin/env python3
"""Render a one-page résumé PDF from a JSON payload, using the skill's fixed
visual template (serif, blue links, black-underlined company names).

Usage: python3 render_resume.py <data.json> <out.pdf>

Expected JSON shape:
{
  "title": "<Name> Resume",
  "basics": { "name": "", "headline": "", "location": "", "phone": "", "email": "",
              "links": [{ "label": "", "url": "" }] },
  "objective": "",
  "skillGroups": [{ "category": "", "items": [""] }],
  "experience": [{ "role": "", "company": "", "companyUrl": "", "period": "", "highlights": [""] }],
  "projects": [{ "slug": "", "name": "", "liveUrl": "", "technologies": "", "highlights": [""] }],
  "education": { "degree": "", "institution": "", "period": "", "gpaOrHonors": "" },
  "languages": [""],
  "strengths": [""]
}

`companyUrl` is optional per experience entry — only set it when you have a
real company URL; never guess one. When omitted, the company name renders as
plain bold text with no link.
"""
import json
import sys

from weasyprint import HTML


def esc(s):
    return (s or "").replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def bullets(items):
    return "".join(f"<li>{esc(i)}</li>" for i in items)


def render(data):
    basics = data["basics"]
    links_html = " | ".join(
        f'<a href="{l["url"]}">{esc(l["label"])}</a>' for l in basics.get("links", [])
    )

    experience_html = ""
    for it in data.get("experience", []):
        company = (
            f'<a href="{it["companyUrl"]}">{esc(it["company"])}</a>'
            if it.get("companyUrl")
            else esc(it["company"])
        )
        experience_html += f'''
<p class="entry-head"><span class="job-title">{esc(it["role"])} &ndash; {company}</span> <span class="job-dates">({esc(it["period"])})</span></p>
<ul>{bullets(it["highlights"])}</ul>'''

    projects_html = ""
    for p in data.get("projects", []):
        title = (
            f'<a href="{p["liveUrl"]}">{esc(p["name"])}</a>'
            if p.get("liveUrl")
            else esc(p["name"])
        )
        projects_html += f'''
<p class="proj-title entry-head">{title} <span class="proj-stack">({esc(p["technologies"])})</span></p>
<ul>{bullets(p["highlights"])}</ul>'''

    skills_html = "".join(
        f'<p><b>{esc(s["category"])}:</b> {esc(", ".join(s["items"]))}</p>'
        for s in data.get("skillGroups", [])
    )
    edu = data["education"]
    edu_extra = f' | {esc(edu["gpaOrHonors"])}' if edu.get("gpaOrHonors") else ""
    lang_strength_line = ""
    if data.get("languages") or data.get("strengths"):
        parts = []
        if data.get("languages"):
            parts.append(f'Languages: {esc(", ".join(data["languages"]))}')
        if data.get("strengths"):
            parts.append(f'Strengths: {esc(", ".join(data["strengths"]))}')
        lang_strength_line = f'<p>{" | ".join(parts)}</p>'

    return f"""<!DOCTYPE html>
<html><head><meta charset="utf-8"><style>
  @page {{ size: Letter; margin: 0.35in 0.7in; }}
  * {{ box-sizing: border-box; }}
  body {{ font-family: 'Liberation Serif', 'Times New Roman', Times, serif; color: #000; font-size: 9.85pt; line-height: 1.15; }}
  a {{ color: #1155cc; text-decoration: underline; }}
  .job-title a {{ color: #000; text-decoration: underline; }}
  .name {{ font-weight: bold; font-size: 12.5pt; margin: 0; }}
  .title {{ font-weight: bold; margin: 1px 0 0 0; }}
  .contact {{ margin: 1px 0 0 0; }}
  .links {{ margin: 1px 0 0 0; }}
  .links a {{ margin-right: 3px; }}
  hr.top {{ border: none; border-top: 1px solid #000; margin: 5px 0 5px 0; }}
  hr.section {{ border: none; border-top: 0.75px solid #999; margin: 1px 0 3px 0; }}
  h2.section {{ font-size: 10.4pt; font-weight: bold; margin: 5px 0 0 0; }}
  p.summary {{ margin: 0; text-align: justify; }}
  .job-title {{ font-weight: bold; }}
  .job-dates {{ font-style: italic; font-weight: normal; }}
  p.entry-head {{ margin: 4px 0 0 0; }}
  ul {{ margin: 1px 0 0 0; padding-left: 18px; }}
  li {{ margin-bottom: 0px; text-align: justify; }}
  .proj-title {{ font-weight: bold; }}
  .proj-title a {{ font-weight: bold; }}
  .proj-stack {{ font-style: italic; font-weight: normal; }}
  .skills p {{ margin: 2px 0; }}
  .edu p {{ margin: 2px 0; }}
</style></head><body>
<p class="name">{esc(basics["name"]).upper()}</p>
<p class="title">{esc(basics["headline"])}</p>
<p class="contact">{esc(basics["location"])} | {esc(basics["phone"])} | {esc(basics["email"])}</p>
<p class="links">{links_html}</p>
<hr class="top">
<h2 class="section">Summary</h2><hr class="section">
<p class="summary">{esc(data["objective"])}</p>
<h2 class="section">Experience</h2><hr class="section">
{experience_html}
<h2 class="section">Projects</h2><hr class="section">
{projects_html}
<h2 class="section">Core Skills</h2><hr class="section">
<div class="skills">{skills_html}</div>
<h2 class="section">Education</h2><hr class="section">
<div class="edu">
<p>{esc(edu["degree"])} | {esc(edu["institution"])} | {esc(edu["period"])}{edu_extra}</p>
{lang_strength_line}
</div>
</body></html>"""


def main():
    if len(sys.argv) != 3:
        print("usage: python3 render_resume.py <data.json> <out.pdf>")
        sys.exit(1)
    data = json.load(open(sys.argv[1]))
    HTML(string=render(data)).write_pdf(sys.argv[2])
    print("written", sys.argv[2])


if __name__ == "__main__":
    main()
