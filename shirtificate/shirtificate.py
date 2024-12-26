from fpdf import FPDF

name = input("Name: ")

pdf = FPDF()
pdf.add_page()
pdf.image("shirtificate.png", w = 185, x = 10, y = 70)
pdf.output("shirtificate.pdf")
