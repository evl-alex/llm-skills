#!/usr/bin/env python3
"""Build a styled market-analysis PDF from a JSON report description.

Usage:
    python3 build_pdf.py report.json output.pdf

JSON schema:
{
  "title": "Market & Marketing Analysis: AppName",   # & is fine here (plain string)
  "subtitle": "US-first iOS launch · $4.99/mo · June 2026",
  "summary": "Bold-lead summary paragraph. Supports <b>/<i> markup; escape & as &amp;",
  "sections": [
    {
      "heading": "1. Market size",
      "blocks": [
        {"type": "paragraph", "text": "..."},
        {"type": "bullets", "items": ["...", "..."]},
        {"type": "table",
         "header": ["Col A", "Col B"],
         "rows": [["...", "..."]],
         "widths": [1, 3]}          # relative column widths, optional
      ]
    }
  ],
  "footer_notes": ["Sources: ...", "Disclaimer ..."]
}

Notes for the generating model:
- In "summary", paragraph/bullet/cell text: escape & as &amp;; <b>, <i>, <sub>,
  <super> tags are supported (reportlab markup). No other HTML.
- Mark a table row as a total row by wrapping every cell in <b>...</b>; striping
  still applies, bold carries the emphasis.
- Keep cells terse in tables with 4+ columns.
"""
import json
import sys

from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.platypus import (HRFlowable, Paragraph, SimpleDocTemplate,
                                Spacer, Table, TableStyle)

ACCENT = colors.HexColor("#1a5276")
LIGHT = colors.HexColor("#eaf2f8")
GRID = colors.HexColor("#b0c4d4")
MUTED = colors.HexColor("#566573")

ss = getSampleStyleSheet()
S = {
    "title": ParagraphStyle("Tx", parent=ss["Title"], fontSize=20,
                            textColor=ACCENT, spaceAfter=2),
    "subtitle": ParagraphStyle("Sx", parent=ss["Normal"], fontSize=10,
                               textColor=MUTED, spaceAfter=10),
    "h1": ParagraphStyle("H1x", parent=ss["Heading1"], fontSize=15,
                         spaceBefore=18, spaceAfter=6, textColor=ACCENT),
    "body": ParagraphStyle("Bx", parent=ss["Normal"], fontSize=9.5,
                           leading=13.5, spaceAfter=5, alignment=TA_LEFT),
    "cell": ParagraphStyle("Cx", parent=ss["Normal"], fontSize=8.5, leading=11),
    "note": ParagraphStyle("Nx", parent=ss["Normal"], fontSize=8, leading=11,
                           textColor=MUTED),
}
S["bullet"] = ParagraphStyle("Blx", parent=S["body"], leftIndent=14,
                             bulletIndent=4)
S["cellh"] = ParagraphStyle("CHx", parent=S["cell"], textColor=colors.white,
                            fontName="Helvetica-Bold")

CONTENT_WIDTH = 7.1 * inch  # letter minus 0.7" margins


def make_table(block):
    header = block["header"]
    rows = block["rows"]
    ncols = len(header)
    rel = block.get("widths") or [1] * ncols
    total = float(sum(rel))
    widths = [CONTENT_WIDTH * w / total for w in rel]

    data = [[Paragraph(str(c), S["cellh"]) for c in header]]
    data += [[Paragraph(str(c), S["cell"]) for c in row] for row in rows]
    t = Table(data, colWidths=widths, repeatRows=1)
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), ACCENT),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, LIGHT]),
        ("GRID", (0, 0), (-1, -1), 0.5, GRID),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("TOPPADDING", (0, 0), (-1, -1), 4),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
    ]))
    return t


def build(spec, out_path):
    story = []
    story.append(Paragraph(spec["title"].replace("&", "&amp;"), S["title"]))
    if spec.get("subtitle"):
        story.append(Paragraph(spec["subtitle"], S["subtitle"]))
    story.append(HRFlowable(width="100%", thickness=1, color=ACCENT))
    story.append(Spacer(1, 8))
    if spec.get("summary"):
        story.append(Paragraph(spec["summary"], S["body"]))

    for sec in spec.get("sections", []):
        story.append(Paragraph(sec["heading"].replace("&", "&amp;"), S["h1"]))
        for block in sec.get("blocks", []):
            btype = block["type"]
            if btype == "paragraph":
                story.append(Paragraph(block["text"], S["body"]))
            elif btype == "bullets":
                for item in block["items"]:
                    story.append(Paragraph(item, S["bullet"], bulletText="•"))
            elif btype == "table":
                story.append(make_table(block))
                story.append(Spacer(1, 4))
            else:
                raise ValueError(f"Unknown block type: {btype}")

    notes = spec.get("footer_notes", [])
    if notes:
        story.append(Spacer(1, 12))
        story.append(HRFlowable(width="100%", thickness=0.5, color=GRID))
        story.append(Spacer(1, 6))
        for n in notes:
            story.append(Paragraph(n, S["note"]))

    doc = SimpleDocTemplate(out_path, pagesize=letter,
                            topMargin=0.7 * inch, bottomMargin=0.7 * inch,
                            leftMargin=0.7 * inch, rightMargin=0.7 * inch,
                            title=spec["title"])
    doc.build(story)


def main():
    if len(sys.argv) != 3:
        sys.exit("Usage: build_pdf.py report.json output.pdf")
    with open(sys.argv[1], encoding="utf-8") as f:
        spec = json.load(f)
    build(spec, sys.argv[2])
    print("OK:", sys.argv[2])


if __name__ == "__main__":
    main()
