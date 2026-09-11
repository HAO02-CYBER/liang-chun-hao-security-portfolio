from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.platypus import HRFlowable, Paragraph, SimpleDocTemplate, Spacer, Table, TableStyle


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "public" / "Liang-Chun-Hao-Resume.pdf"

INK = colors.HexColor("#101722")
TEXT = colors.HexColor("#28313d")
MUTED = colors.HexColor("#607086")
ACCENT = colors.HexColor("#167a8b")
PALE = colors.HexColor("#eaf4f5")
LINE = colors.HexColor("#cbd8dd")


def p(text, style):
    return Paragraph(text, style)


def section(title, styles):
    return [
        Spacer(1, 2.2 * mm),
        p(title.upper(), styles["section"]),
        Spacer(1, 1.4 * mm),
    ]


def build():
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    doc = SimpleDocTemplate(
        str(OUTPUT),
        pagesize=A4,
        rightMargin=15 * mm,
        leftMargin=15 * mm,
        topMargin=12 * mm,
        bottomMargin=9 * mm,
        title="LIANG CHUN HAO - Security Technology Resume",
        author="LIANG CHUN HAO",
    )

    sample = getSampleStyleSheet()
    styles = {
        "name": ParagraphStyle("Name", parent=sample["Heading1"], fontName="Helvetica-Bold", fontSize=23, leading=25, textColor=colors.white, spaceAfter=1),
        "target": ParagraphStyle("Target", parent=sample["BodyText"], fontName="Helvetica-Bold", fontSize=8.4, leading=10, textColor=PALE, tracking=0.35),
        "contact": ParagraphStyle("Contact", parent=sample["BodyText"], fontName="Helvetica", fontSize=8.1, leading=10.5, textColor=colors.white, alignment=2),
        "summary": ParagraphStyle("Summary", parent=sample["BodyText"], fontName="Helvetica", fontSize=9.15, leading=12.1, textColor=TEXT),
        "section": ParagraphStyle("Section", parent=sample["Heading2"], fontName="Helvetica-Bold", fontSize=8.05, leading=9.5, textColor=ACCENT, tracking=0.55),
        "role": ParagraphStyle("Role", parent=sample["BodyText"], fontName="Helvetica-Bold", fontSize=9.2, leading=11.1, textColor=INK),
        "meta": ParagraphStyle("Meta", parent=sample["BodyText"], fontName="Helvetica-Bold", fontSize=7.7, leading=9.4, textColor=MUTED, tracking=0.2),
        "body": ParagraphStyle("Body", parent=sample["BodyText"], fontName="Helvetica", fontSize=8, leading=9.75, textColor=TEXT, spaceAfter=0.8),
        "small": ParagraphStyle("Small", parent=sample["BodyText"], fontName="Helvetica", fontSize=7.85, leading=9.6, textColor=TEXT),
        "skill": ParagraphStyle("Skill", parent=sample["BodyText"], fontName="Helvetica", fontSize=8, leading=10.1, textColor=TEXT),
    }

    story = []
    header = Table(
        [[
            [p("LIANG CHUN HAO", styles["name"]), p("SECURITY TECHNOLOGY STUDENT | PENTESTING | CLOUD SECURITY | NETWORK SECURITY", styles["target"])],
            p("chunhao021223@icloud.com<br/>+60 10-362 3937<br/>github.com/HAO02-CYBER", styles["contact"]),
        ]],
        colWidths=[118 * mm, 61 * mm],
        rowHeights=[26 * mm],
    )
    header.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), INK),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("LEFTPADDING", (0, 0), (0, 0), 7 * mm),
        ("RIGHTPADDING", (0, 0), (0, 0), 3 * mm),
        ("LEFTPADDING", (1, 0), (1, 0), 3 * mm),
        ("RIGHTPADDING", (1, 0), (1, 0), 7 * mm),
        ("TOPPADDING", (0, 0), (-1, -1), 0),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 0),
    ]))
    story.extend([header, Spacer(1, 3 * mm), HRFlowable(width="100%", thickness=1.3, color=ACCENT)])

    story += section("Profile", styles)
    story.append(p(
        "Security Technology undergraduate seeking an internship in penetration testing, cloud security, or network security. Practical foundations include vulnerability assessment, least-privilege reviews, cryptography, malware behavior analysis, and clear security documentation.",
        styles["summary"],
    ))

    story += section("Education", styles)
    story.append(p("MULTIMEDIA UNIVERSITY, Faculty of Information Science & Technology", styles["role"]))
    story.append(p("Bachelor of Information Technology (Honours), Security Technology", styles["meta"]))
    education = Table([
        [p("CURRENT CGPA", styles["meta"]), p("3.79", styles["role"]), p("ACADEMIC RECOGNITION", styles["meta"]), p("Dean's List, 2x", styles["role"])],
        [p("RELEVANT STUDY", styles["meta"]), p("Ethical Hacking, Applied Cryptography, Digital Forensics, Computer Security, Cybersecurity Law", styles["small"]), "", ""],
    ], colWidths=[27 * mm, 35 * mm, 40 * mm, 77 * mm])
    education.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), PALE), ("VALIGN", (0, 0), (-1, -1), "MIDDLE"), ("SPAN", (1, 1), (3, 1)),
        ("TOPPADDING", (0, 0), (-1, -1), 2.2 * mm), ("BOTTOMPADDING", (0, 0), (-1, -1), 2.2 * mm),
        ("LEFTPADDING", (0, 0), (-1, -1), 3 * mm), ("RIGHTPADDING", (0, 0), (-1, -1), 3 * mm),
        ("LINEBELOW", (0, 0), (-1, 0), 0.35, LINE),
    ]))
    story.extend([Spacer(1, 1.4 * mm), education])

    story += section("Security Capabilities", styles)
    skills = Table([
        [p("<b>Pentesting Foundations</b><br/>Reconnaissance, weakness validation, risk rating, remediation notes", styles["skill"]), p("<b>Cloud and Network Security</b><br/>Identity, least privilege, storage, exposure, logging, baseline reviews", styles["skill"])],
        [p("<b>Analysis and Defense</b><br/>Malware behavior indicators, persistence ideas, defensive signals", styles["skill"]), p("<b>Security Principles</b><br/>Hashing, encryption, authentication, key handling, cybersecurity law", styles["skill"])],
    ], colWidths=[89.5 * mm, 89.5 * mm])
    skills.setStyle(TableStyle([
        ("VALIGN", (0, 0), (-1, -1), "TOP"), ("BOX", (0, 0), (-1, -1), 0.5, LINE), ("INNERGRID", (0, 0), (-1, -1), 0.35, LINE),
        ("TOPPADDING", (0, 0), (-1, -1), 2.4 * mm), ("BOTTOMPADDING", (0, 0), (-1, -1), 2.4 * mm),
        ("LEFTPADDING", (0, 0), (-1, -1), 3 * mm), ("RIGHTPADDING", (0, 0), (-1, -1), 3 * mm),
    ]))
    story.append(skills)

    story += section("Selected Security Labs", styles)
    labs = [
        ("Vulnerability Assessment Lab", "Reconnaissance, weakness validation, risk rating, and remediation evidence writing."),
        ("Cloud Security Baseline Study", "Identity, storage, network exposure, logging, and least-privilege reviews."),
        ("Malware Behavior Analysis Notes", "Suspicious behavior, indicators, persistence ideas, and defensive observations."),
    ]
    for title, detail in labs:
        story.extend([p(title, styles["role"]), p(detail, styles["body"])])

    story += section("Experience", styles)
    experience = Table([
        [p("2023 - 2024", styles["meta"]), p("IT Support | Singapore", styles["role"])],
        ["", p("Supported technical troubleshooting, device readiness, and day-to-day user assistance in a professional environment.", styles["body"])],
        [p("2022 - 2023", styles["meta"]), p("Administrative Assistant | Singapore", styles["role"])],
        ["", p("Handled operational coordination, documentation, and clear communication with accuracy and follow-through.", styles["body"])],
    ], colWidths=[29 * mm, 150 * mm])
    experience.setStyle(TableStyle([
        ("VALIGN", (0, 0), (-1, -1), "TOP"), ("TOPPADDING", (0, 0), (-1, -1), 0), ("BOTTOMPADDING", (0, 0), (-1, -1), 1.2 * mm),
        ("LEFTPADDING", (0, 0), (-1, -1), 0), ("RIGHTPADDING", (0, 0), (-1, -1), 0),
    ]))
    story.append(experience)

    story += section("Additional Evidence", styles)
    evidence = Table([
        [p("MUET", styles["meta"]), p("4.0 | CEFR B2", styles["small"]), p("ACTIVITIES", styles["meta"]), p("PROSOLVE NATIONAL 2025 | Infineon Interview Event volunteer | MMU IT Club and Dragon Boat Club", styles["small"])],
    ], colWidths=[33 * mm, 47 * mm, 35 * mm, 64 * mm])
    evidence.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), colors.HexColor("#f5f8f8")), ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("TOPPADDING", (0, 0), (-1, -1), 2.1 * mm), ("BOTTOMPADDING", (0, 0), (-1, -1), 2.1 * mm),
        ("LEFTPADDING", (0, 0), (-1, -1), 3 * mm), ("RIGHTPADDING", (0, 0), (-1, -1), 3 * mm),
    ]))
    story.append(evidence)

    doc.build(story)
    print(OUTPUT)


if __name__ == "__main__":
    build()
