from pathlib import Path

from reportlab.lib.colors import HexColor
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfgen import canvas


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "public" / "Liang-Chun-Hao-Resume.pdf"

PAPER = HexColor("#F6F6F1")
INK = HexColor("#10100F")
MUTED = HexColor("#6E6E67")
LINE = HexColor("#D8D8D0")
PANEL = HexColor("#FFFFFF")
LIME = HexColor("#C7D535")
ACCENT = HexColor("#7A8608")
SOFT = HexColor("#E9E9E1")
WHITE = HexColor("#FFFFFF")


def split_lines(text, font_name, font_size, max_width):
    words = text.split()
    lines = []
    current = ""
    for word in words:
        candidate = word if not current else f"{current} {word}"
        if pdfmetrics.stringWidth(candidate, font_name, font_size) <= max_width:
            current = candidate
        else:
            if current:
                lines.append(current)
            current = word
    if current:
        lines.append(current)
    return lines


def draw_wrapped(c, text, x, top, max_width, font_name="Helvetica", font_size=8.4,
                 leading=11.2, color=INK, max_lines=None):
    lines = split_lines(text, font_name, font_size, max_width)
    if max_lines is not None:
        lines = lines[:max_lines]
    c.setFillColor(color)
    c.setFont(font_name, font_size)
    for index, line in enumerate(lines):
        c.drawString(x, top - font_size - index * leading, line)
    return top - len(lines) * leading


def draw_label(c, text, x, top, color=ACCENT):
    c.setFillColor(color)
    c.setFont("Courier-Bold", 7.1)
    c.drawString(x, top - 7.1, text.upper())
    return top - 15


def draw_rule(c, x, y, width, color=LINE):
    c.setStrokeColor(color)
    c.setLineWidth(0.65)
    c.line(x, y, x + width, y)


def draw_metric(c, x, top, width, label, value, detail):
    c.setFillColor(PANEL)
    c.roundRect(x, top - 64, width, 64, 6, fill=1, stroke=0)
    c.setFillColor(MUTED)
    c.setFont("Courier-Bold", 6.5)
    c.drawString(x + 12, top - 16, label.upper())
    c.setFillColor(INK)
    c.setFont("Helvetica-Bold", 20)
    c.drawString(x + 12, top - 40, value)
    c.setFillColor(MUTED)
    c.setFont("Helvetica", 6.8)
    c.drawRightString(x + width - 12, top - 38, detail)


def draw_entry(c, number, title, description, x, top, width):
    c.setFillColor(ACCENT)
    c.setFont("Courier-Bold", 7)
    c.drawString(x, top - 8, number)
    c.setFillColor(INK)
    c.setFont("Helvetica-Bold", 9.4)
    c.drawString(x + 24, top - 9, title)
    bottom = draw_wrapped(c, description, x + 24, top - 16, width - 24,
                          font_size=7.5, leading=9.7, color=MUTED, max_lines=2)
    return bottom - 9


def draw_capability(c, title, text, x, top, width):
    c.setFillColor(INK)
    c.setFont("Helvetica-Bold", 8.1)
    c.drawString(x, top - 8, title)
    return draw_wrapped(c, text, x, top - 12, width, font_size=7.25,
                        leading=9.3, color=MUTED, max_lines=3) - 8


def build_resume():
    width, height = A4
    c = canvas.Canvas(str(OUTPUT), pagesize=A4, pageCompression=1)
    c.setTitle("LIANG CHUN HAO - Security Technology Resume")
    c.setAuthor("LIANG CHUN HAO")
    c.setSubject("Internship resume for pentesting, cloud security, and network security")
    c.setCreator("LIANG CHUN HAO Portfolio")

    c.setFillColor(PAPER)
    c.rect(0, 0, width, height, fill=1, stroke=0)

    margin = 34
    content_width = width - margin * 2
    header_top = height - 28
    header_height = 114
    header_bottom = header_top - header_height

    c.setFillColor(INK)
    c.roundRect(margin, header_bottom, content_width, header_height, 8, fill=1, stroke=0)

    left = margin + 20
    c.setFillColor(WHITE)
    c.setFont("Helvetica-Bold", 25)
    c.drawString(left, header_top - 34, "LIANG CHUN HAO")
    c.setFont("Helvetica-Bold", 8.5)
    c.drawString(left, header_top - 55, "SECURITY TECHNOLOGY STUDENT")
    c.setFillColor(HexColor("#D5D5CC"))
    c.setFont("Helvetica", 7.7)
    c.drawString(left, header_top - 72, "Pentesting  /  Cloud Security  /  Network Security")

    c.setFillColor(LIME)
    c.circle(left + 3, header_bottom + 16, 3, fill=1, stroke=0)
    c.setFillColor(WHITE)
    c.setFont("Courier-Bold", 6.7)
    c.drawString(left + 12, header_bottom + 13.5, "OPEN TO 2026 INTERNSHIP OPPORTUNITIES")

    contact_right = margin + content_width - 20
    contact_top = header_top - 25
    contacts = [
        ("chunhao021223@icloud.com", "mailto:chunhao021223@icloud.com"),
        ("github.com/HAO02-CYBER", "https://github.com/HAO02-CYBER"),
        ("liang-chun-hao-security-portfolio.vercel.app", "https://liang-chun-hao-security-portfolio.vercel.app/"),
        ("WhatsApp  +60 10-362 3937", "https://wa.me/60103623937"),
    ]
    c.setFont("Helvetica", 7.2)
    for index, (label, url) in enumerate(contacts):
        y = contact_top - index * 15
        label_width = pdfmetrics.stringWidth(label, "Helvetica", 7.2)
        x = contact_right - label_width
        c.setFillColor(HexColor("#E7E7DF"))
        c.drawString(x, y, label)
        c.linkURL(url, (x, y - 2, contact_right, y + 8), relative=0)

    profile_top = header_bottom - 18
    draw_label(c, "Profile / 01", margin, profile_top)
    profile = (
        "Security Technology undergraduate seeking an internship in penetration testing, cloud security, or network security. "
        "Building practical foundations in vulnerability assessment, least-privilege review, malware behavior analysis, "
        "cryptography, and clear security documentation."
    )
    draw_wrapped(c, profile, margin, profile_top - 13, content_width, font_size=8.6,
                 leading=11.8, color=INK, max_lines=3)

    metric_top = profile_top - 59
    draw_label(c, "Academic proof / 02", margin, metric_top)
    metric_top -= 17
    c.setFillColor(SOFT)
    c.roundRect(margin, metric_top - 72, content_width, 72, 7, fill=1, stroke=0)
    gap = 7
    metric_width = (content_width - 16 - gap * 2) / 3
    metric_x = margin + 8
    draw_metric(c, metric_x, metric_top - 4, metric_width, "Current CGPA", "3.79", "B.IT (Hons.)")
    draw_metric(c, metric_x + metric_width + gap, metric_top - 4, metric_width, "Dean's List", "2x", "2025")
    draw_metric(c, metric_x + (metric_width + gap) * 2, metric_top - 4, metric_width, "MUET Band", "4.0", "CEFR B2")

    columns_top = metric_top - 91
    left_width = 322
    column_gap = 22
    right_x = margin + left_width + column_gap
    right_width = content_width - left_width - column_gap

    y_left = draw_label(c, "Selected security labs / 03", margin, columns_top)
    y_left = draw_entry(c, "01", "Vulnerability Assessment", "Reconnaissance, weakness validation, risk rating, and remediation evidence writing.", margin, y_left, left_width)
    y_left = draw_entry(c, "02", "Cloud Security Baseline", "Identity, storage, network exposure, logging, and least-privilege review.", margin, y_left, left_width)
    y_left = draw_entry(c, "03", "Malware Behavior Analysis", "Suspicious behavior, indicators, persistence ideas, and defensive observations.", margin, y_left, left_width)

    draw_rule(c, margin, y_left + 1, left_width)
    y_left -= 13
    y_left = draw_label(c, "Experience / 04", margin, y_left)

    c.setFillColor(MUTED)
    c.setFont("Courier-Bold", 6.7)
    c.drawString(margin, y_left - 8, "2023 - 2024  /  SINGAPORE")
    c.setFillColor(INK)
    c.setFont("Helvetica-Bold", 9.2)
    c.drawString(margin, y_left - 23, "IT Support")
    y_left = draw_wrapped(c, "Technical troubleshooting, device readiness, and day-to-day user support in a professional environment.", margin, y_left - 28, left_width, font_size=7.5, leading=9.7, color=MUTED, max_lines=2) - 12

    c.setFillColor(MUTED)
    c.setFont("Courier-Bold", 6.7)
    c.drawString(margin, y_left - 8, "2022 - 2023  /  SINGAPORE")
    c.setFillColor(INK)
    c.setFont("Helvetica-Bold", 9.2)
    c.drawString(margin, y_left - 23, "Administrative Assistant")
    y_left = draw_wrapped(c, "Operational coordination, documentation, and accurate communication with consistent follow-through.", margin, y_left - 28, left_width, font_size=7.5, leading=9.7, color=MUTED, max_lines=2) - 8

    y_right = draw_label(c, "Education / 05", right_x, columns_top)
    c.setFillColor(INK)
    c.setFont("Helvetica-Bold", 9)
    c.drawString(right_x, y_right - 8, "MULTIMEDIA UNIVERSITY")
    y_right = draw_wrapped(c, "Bachelor of Information Technology (Honours), Security Technology", right_x, y_right - 13, right_width, font_size=7.4, leading=9.6, color=MUTED, max_lines=3) - 8

    draw_rule(c, right_x, y_right + 1, right_width)
    y_right -= 13
    y_right = draw_label(c, "Core capabilities / 06", right_x, y_right)
    y_right = draw_capability(c, "Pentesting foundations", "Reconnaissance, validation, risk rating, remediation notes", right_x, y_right, right_width)
    y_right = draw_capability(c, "Cloud and network", "Identity, least privilege, storage exposure, logging, baselines", right_x, y_right, right_width)
    y_right = draw_capability(c, "Analysis and defense", "Malware indicators, persistence ideas, defensive signals", right_x, y_right, right_width)
    y_right = draw_capability(c, "Security principles", "Hashing, encryption, authentication, key handling", right_x, y_right, right_width)

    draw_rule(c, right_x, y_right + 1, right_width)
    y_right -= 13
    y_right = draw_label(c, "Relevant study / 07", right_x, y_right)
    y_right = draw_wrapped(c, "Ethical Hacking / Applied Cryptography / Digital Forensics / Computer Security / Cybersecurity Law", right_x, y_right - 1, right_width, font_size=7.35, leading=9.8, color=INK, max_lines=5) - 10

    draw_rule(c, right_x, y_right + 1, right_width)
    y_right -= 13
    y_right = draw_label(c, "Activities / 08", right_x, y_right)
    draw_wrapped(c, "PROSOLVE National 2025 / Infineon Interview Event volunteer / MMU IT Club / Dragon Boat Club", right_x, y_right - 1, right_width, font_size=7.35, leading=9.8, color=INK, max_lines=5)

    footer_y = 25
    c.setFillColor(INK)
    c.roundRect(margin, footer_y, content_width, 28, 6, fill=1, stroke=0)
    c.setFillColor(WHITE)
    c.setFont("Courier-Bold", 6.5)
    c.drawString(margin + 13, footer_y + 10, "PORTFOLIO / 2026")
    footer_url = "liang-chun-hao-security-portfolio.vercel.app"
    c.setFont("Helvetica-Bold", 6.9)
    c.drawRightString(margin + content_width - 13, footer_y + 10, footer_url)
    url_width = pdfmetrics.stringWidth(footer_url, "Helvetica-Bold", 6.9)
    c.linkURL(
        "https://liang-chun-hao-security-portfolio.vercel.app/",
        (margin + content_width - 13 - url_width, footer_y + 7, margin + content_width - 13, footer_y + 19),
        relative=0,
    )

    c.showPage()
    c.save()
    print(OUTPUT)


if __name__ == "__main__":
    build_resume()
