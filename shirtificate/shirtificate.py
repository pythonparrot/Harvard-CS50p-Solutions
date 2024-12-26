from fpdf import FPDF

pdf = FPDF()
pdf.add_page()
pdf.image("shirtificate.png")
pdf.output("shirtificate.pdf")
