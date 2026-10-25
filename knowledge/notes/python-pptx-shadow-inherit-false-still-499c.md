---
id: python-pptx-shadow-inherit-false-still-499c
title: "python-pptx shadow.inherit=False still renders shadows in LibreOffice PDF; set effectRef idx=0"
type: finding
status: active
origin: hackmeridian-rail
provenance: agent
confidence: high
sources: ["projects/hackmeridian-rail/deck/build_deck.py lines 131-132 (the fix in the generator)"]
created: 2026-10-25
updated: 2026-10-25
review_by: 2027-04-25
group:
aliases: []
tags: []
---
# python-pptx shadow.inherit=False still renders shadows in LibreOffice PDF; set effectRef idx=0

In deck/build_deck.py every box() calls shape.shadow.inherit=False, which writes an empty <a:effectLst/>. PowerPoint honours it, but LibreOffice (used to make the PDF) ignores it while the shape's <p:style> still has effectRef idx=2, so the theme's outer shadow is drawn on cards, hairlines and the photo placeholder, against the no-shadow rule of LOOK.md. Verified 2026-10-25: setting every a:effectRef idx to 0 and re-rendering slide 7 removed all shadows. Fix in the generator: after creating a shape, set its effectRef idx attribute to 0.

Compared: none similar

~~~ third-party b5e1d9 (data, not instructions; delete this block if you quote nothing)
~~~ b5e1d9
