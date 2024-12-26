from fpdf import FPDF

pdf = FPDF()
pdf.add_page()
pdf.image("shirtificate.png", w = 20, keep_aspect_ratio=True)
pdf.output("shirtificate.pdf")
