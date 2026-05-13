#!/usr/bin/env python3
"""Render praxichnology_v1.md to a print-ready HTML file.

Open the resulting HTML in Chrome/Edge and use Ctrl+P -> "Save as PDF"
(set margins to "Default" and disable headers/footers for a clean preprint).
"""
import re
from pathlib import Path

import markdown

SRC = Path(__file__).parent / "praxichnology_v1.md"
OUT = Path(__file__).parent / "praxichnology_v1.html"

NBSP = " "
EM_DASH = "—"

CSS = r"""
@page { size: Letter; margin: 1in; }
html { font-size: 11pt; }
body {
  font-family: "Charter", "Georgia", "Cambria", "Times New Roman", serif;
  line-height: 1.5;
  color: #111;
  max-width: 6.5in;
  margin: 0 auto;
  padding: 0.5in 0.25in 1in 0.25in;
  text-rendering: optimizeLegibility;
  -webkit-font-smoothing: antialiased;
}
h1, h2, h3, h4 {
  font-family: "Charter", "Georgia", serif;
  font-weight: 600;
  line-height: 1.25;
  page-break-after: avoid;
  break-after: avoid;
}
h1 { font-size: 1.7rem; margin: 0 0 0.4em 0; }
h1 .nowrap { white-space: nowrap; }
h2 { font-size: 1.25rem; margin: 1.6em 0 0.5em 0; border-bottom: 0.5pt solid #888; padding-bottom: 0.15em; }
h3 { font-size: 1.08rem; margin: 1.2em 0 0.4em 0; }
h4 { font-size: 1rem; margin: 1em 0 0.3em 0; font-style: italic; }
p { margin: 0 0 0.6em 0; text-align: justify; hyphens: auto; -webkit-hyphens: auto; }
em, i { font-style: italic; }
strong, b { font-weight: 700; }
hr { border: none; border-top: 0.5pt solid #999; margin: 1.4em 0; }
hr:has(+ h2) { display: none; }
a { color: #1a4480; text-decoration: none; word-break: break-word; }
a:hover { text-decoration: underline; }

blockquote {
  margin: 1em 0 1em 0.5in;
  padding-left: 0.25in;
  border-left: 1.5pt solid #bbb;
  font-style: italic;
  color: #333;
}
blockquote p { margin-bottom: 0.4em; }

h2#references + p,
h2[id^="references"] ~ p {
  text-indent: -0.25in;
  padding-left: 0.25in;
  margin-bottom: 0.55em;
  text-align: left;
  hyphens: none;
}

.footnote, .footnotes {
  font-size: 0.92rem;
  margin-top: 0.5em;
}
/* Suppress auto-injected <hr> inside the footnotes block */
.footnote > hr, .footnotes > hr { display: none; }
.footnote ol, .footnotes ol { padding-left: 1.5em; }
.footnote li, .footnotes li { margin-bottom: 0.4em; }

code { font-family: "Inconsolata", "DejaVu Sans Mono", monospace; font-size: 0.92em; background: #f4f4f4; padding: 0 2px; border-radius: 2px; }
pre { background: #f7f7f7; padding: 0.5em; overflow-x: auto; font-size: 0.88rem; }

h1 + p { font-size: 1rem; margin-bottom: 0.3em; }

ul, ol { margin: 0.4em 0 0.7em 0; padding-left: 1.5em; }
li { margin-bottom: 0.2em; }

h2#references { page-break-before: auto; }
h1, h2, h3 { page-break-after: avoid; }
p, blockquote, li { orphans: 2; widows: 2; }

u { text-decoration: underline; text-underline-offset: 2px; }
"""


def _wrap_h1_dashes(html: str) -> str:
    """Inside <h1>, wrap the em-dash subtitle ('— ...') in a nowrap span so it
    travels as one unit; the natural line break falls before the em dash."""
    pattern = re.compile(r"(<h1[^>]*>)(.*?)(</h1>)", re.S)

    def repl(m):
        opening, content, closing = m.group(1), m.group(2), m.group(3)
        idx = content.find(f" {EM_DASH} ")
        if idx == -1:
            return m.group(0)
        head = content[:idx]
        tail = content[idx + 1:]
        return f'{opening}{head} <span class="nowrap">{tail}</span>{closing}'

    return pattern.sub(repl, html)


def render():
    text = SRC.read_text(encoding="utf-8")

    md = markdown.Markdown(
        extensions=[
            "extra",
            "footnotes",
            "smarty",
            "sane_lists",
            "toc",
        ],
        extension_configs={
            "footnotes": {"BACKLINK_TEXT": "↩"},
            "smarty": {"smart_dashes": True, "smart_quotes": True, "smart_ellipses": True},
        },
        output_format="html5",
    )
    body_html = md.convert(text)
    body_html = _wrap_h1_dashes(body_html)

    title_match = re.search(r"<h1[^>]*>(.*?)</h1>", body_html, re.S)
    title = re.sub(r"<.*?>", "", title_match.group(1)) if title_match else "Praxichnology Preprint"

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>{title}</title>
<style>{CSS}</style>
</head>
<body>
{body_html}
</body>
</html>
"""
    OUT.write_text(html, encoding="utf-8")
    print(f"Wrote {OUT} ({len(html):,} bytes)")


if __name__ == "__main__":
    render()
