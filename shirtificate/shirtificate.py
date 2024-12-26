from fpdf import FPDF

pdf = FPDF()
pdf.add_page()
pdf.image("shirtificate.png", x = pdf.eph/2, h = pdf.epw/2)
pdf.output("shirtificate.pdf")
