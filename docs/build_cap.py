# -*- coding: utf-8 -*-
"""Benchmark Contract Services LLC - 1-page Capability Statement."""
import os
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.pdfgen import canvas

NAVY   = colors.HexColor('#0F2740')
STEEL  = colors.HexColor('#2E6A8E')
WHITE  = colors.white
LIGHT  = colors.HexColor('#E8EEF3')
MUTED  = colors.HexColor('#5B6B7A')

W, H = letter  # 612 x 792
M = 0.55 * inch
CW = W - 2 * M

OUT = r"C:\BCS\app\docs\Capability-Statement.pdf"

c = canvas.Canvas(OUT, pagesize=letter)
c.setTitle("Benchmark Contract Services LLC - Capability Statement")

def rect(x, y, w, h, fill, stroke=None, sw=0):
    c.setFillColor(fill)
    if stroke:
        c.setStrokeColor(stroke); c.setLineWidth(sw)
        c.rect(x, y, w, h, stroke=1, fill=1)
    else:
        c.rect(x, y, w, h, stroke=0, fill=1)

def txt(x, y, s, size, fill, font="Helvetica"):
    c.setFont(font, size); c.setFillColor(fill)
    c.drawString(x, y, s)

def txtr(x, y, s, size, fill, font="Helvetica"):
    c.setFont(font, size); c.setFillColor(fill)
    c.drawRightString(x, y, s)

def wrap(s, size, w):
    c.setFont("Helvetica", size)
    return c.splitString(s, w)

# ---------------- HEADER ----------------
y = H - M
rect(M, H - 0.28*inch, CW, 0.16*inch, NAVY)   # top rule
htop = y
# Company name (big)
c.setFillColor(NAVY)
c.setFont("Helvetica-Bold", 24)
c.drawString(M, H - M - 4, "Benchmark Contract Services LLC")
# Brand short
c.setFillColor(STEEL); c.setFont("Helvetica-Bold", 11)
c.drawString(M, H - M - 24, "BUILDING SERVICES  \u2022  CONTRACTING  \u2022  MANAGEMENT  \u2022  \"BCS\"")
# tagline / model line
c.setFillColor(MUTED); c.setFont("Helvetica-Oblique", 9.5)
c.drawString(M, H - M - 38, "One accountable partner between your facility and a qualified network of service providers.")

# Contact block - right side
cbx = W - M
c.setFillColor(NAVY); c.setFont("Helvetica", 9.5)
c.drawRightString(cbx, H - M - 6, "(202) 679-2923")
c.drawRightString(cbx, H - M - 18, "info@benchmarkcontractservices.com")
c.drawRightString(cbx, H - M - 30, "919 E Main St, FL 6, Richmond, VA 23219")

# thin divider under header
rect(M, H - M - 48, CW, 0.015*inch, STEEL)

# ---------------- CREDENTIALS ROW ----------------
cy = H - M - 66
def cred(x, label, value):
    c.setFillColor(STEEL); c.setFont("Helvetica-Bold", 8)
    c.drawString(x, cy + 2, label.upper())
    c.setFillColor(NAVY); c.setFont("Helvetica-Bold", 10)
    c.drawString(x, cy - 10, value)

cred(M, "eVA / Registration ID", "525389")
cred(M + CW*0.30, "SWaM Status (VA SBSD)", "In Progress")
cred(M + CW*0.60, "Insurance Baseline", "GL $1M / $2M")
txtr(cbx, cy - 10, "WC & Employers\u2019 Liab. \u2022 Comm. Auto", 8.5, NAVY, "Helvetica-Bold")

# ---------------- SERVICES ----------------
sy = cy - 38
c.setFillColor(NAVY); c.setFont("Helvetica-Bold", 13)
c.drawString(M, sy, "Service Categories")

serv = [
    "Janitorial & Custodial",
    "Commercial / Interior Painting",
    "Landscaping & Grounds",
    "Pressure Washing & Surface Restoration",
    "Debris Hauling & Waste Removal",
    "Recurring Facility Support",
]
sw2 = CW / 2.0
colx = M
rowy = None
for i, s in enumerate(serv):
    col = i % 2
    row = i // 2
    cx = M + col * sw2
    cyy = sy - 22 - row * 22
    rect(cx, cyy - 13, sw2 - 14, 17, WHITE, STEEL, 0.8)
    c.setFillColor(STEEL)
    tri = [ (cx+5, cyy-2), (cx+10, cyy-2), (cx+7.5, cyy-6.5) ]
    c.setStrokeColor(NAVY); c.setLineWidth(1); c.setLineJoin(1)
    p = c.beginPath(); p.moveTo(*tri[0]); p.lineTo(*tri[1]); p.lineTo(*tri[2]); p.close()
    c.drawPath(p, stroke=0, fill=1)
    c.setFillColor(NAVY); c.setFont("Helvetica-Bold", 9.5)
    c.drawString(cx+14, cyy-3, s)
    rowy = cyy

# ---------------- CODES TABLE ----------------
ty = rowy - 24
c.setFillColor(NAVY); c.setFont("Helvetica-Bold", 13)
c.drawString(M, ty, "Procurement Codes")

def code_table(header_left, header_right, rows_left, rows_right, y0):
    hh = 18
    th = 13
    col1 = M
    colw = (CW - 8) / 2.0
    col2 = M + colw + 8
    # header bar
    rect(M, y0 - hh + 2, CW, hh, NAVY)
    c.setFillColor(WHITE); c.setFont("Helvetica-Bold", 8.5)
    c.drawString(col1+6, y0 - hh + 8, header_left)
    c.drawString(col2+6, y0 - hh + 8, header_right)
    rr = y0 - hh - 2
    for i in range(max(len(rows_left), len(rows_right))):
        l = rows_left[i] if i < len(rows_left) else ("", "")
        r = rows_right[i] if i < len(rows_right) else ("", "")
        yb = rr - th * (i+1)
        if i % 2 == 0:
            rect(M, yb, CW, th, LIGHT)
        c.setFillColor(NAVY); c.setFont("Helvetica-Bold", 8.5)
        c.drawString(col1+6, yb + 4, l[0])
        c.setFillColor(MUTED); c.setFont("Helvetica", 8.5)
        c.drawString(col1+76, yb + 4, l[1])
        c.setFillColor(NAVY); c.setFont("Helvetica-Bold", 8.5)
        c.drawString(col2+6, yb + 4, r[0])
        c.setFillColor(MUTED); c.setFont("Helvetica", 8.5)
        c.drawString(col2+76, yb + 4, r[1])
    return rr - th * max(len(rows_left), len(rows_right))

nlgp = [
    ("910-39", "Janitorial & Custodial Services"),
    ("910-54", "Painting, Maint. & Repair Services"),
    ("988-52", "Landscaping & Grounds Maintenance"),
    ("910-03", "Building Cleaning, Exterior (Pressure Washing)"),
    ("962-86", "Debris Hauling & Bulk Waste Removal"),
    ("958-44", "Facility Management Support Services"),
]
naics = [
    ("561720", "Janitorial Services (Primary)"),
    ("238320", "Painting & Wall Covering Contractors"),
    ("561730", "Landscaping Services"),
    ("561790", "Other Building Services (Pressure Washing)"),
    ("562111", "Solid Waste Collection & Hauling"),
    ("561210", "Facilities Support Services"),
]
by = code_table("NIGP CODES", "NAICS CODES", nlgp, naics, ty - 6)

# ---------------- SERVICE AREA + PROCESS ----------------
ay = by - 16
c.setFillColor(NAVY); c.setFont("Helvetica-Bold", 13)
c.drawString(M, ay, "Service Area")
c.setFillColor(MUTED); c.setFont("Helvetica", 9.5)
c.drawString(M, ay - 14, "Based in Richmond, VA \u2014 serving Central Virginia, the Richmond Metro, and surrounding public & commercial facilities.")

py = ay - 34
c.setFillColor(NAVY); c.setFont("Helvetica-Bold", 13)
c.drawString(M, py, "Our 5-Step Quality Process")
steps = ["Requirement", "Contract\nAlignment", "Service\nCoordination", "Quality\nControl", "Completion"]
stx = M
stw = CW / 5.0
for i, st in enumerate(steps):
    cx = M + i * stw
    rect(cx, py - 26, stw - 8, 30, NAVY)
    # step number
    c.setFillColor(STEEL); c.setFont("Helvetica-Bold", 8)
    c.drawString(cx + 6, py - 6, f"STEP {i+1}")
    c.setFillColor(WHITE); c.setFont("Helvetica-Bold", 9)
    lines = st.split("\n")
    lh = 11
    start = py - 16
    if len(lines) == 1:
        c.drawCentredString(cx + (stw-8)/2, py - 16, st)
    else:
        c.drawString(cx + 6, start + lh - 2, lines[0])
        c.drawString(cx + 6, start - 2, lines[1])

# closeout note
note_y = py - 44
lines = cp = None
c.setFillColor(MUTED); c.setFont("Helvetica-Oblique", 8.5)
c.drawString(M, note_y, "Every project closes with a digital closeout report, an inspection checklist, and single-point-of-contact oversight on every engagement.")

# ---------------- FOOTER ----------------
rect(M, M - 6, CW, 0.02*inch, STEEL)
c.setFillColor(MUTED); c.setFont("Helvetica", 8)
c.drawString(M, M - 18, "Benchmark Contract Services LLC  \u2022  919 E Main St, FL 6, Richmond, VA 23219")
c.drawRightString(W - M, M - 18, "(202) 679-2923 \u2022 info@benchmarkcontractservices.com \u2022 eVA 525389")

c.showPage()
c.save()
print("saved", OUT)