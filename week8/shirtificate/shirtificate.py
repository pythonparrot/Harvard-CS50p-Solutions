from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        # Setting font: helvetica bold 15
        self.set_font("helvetica", style="B", size=50)
        # Moving cursor to the right:
        self.cell(80)
        # Printing title:
        self.cell(30, 10, "CS50 Shirtificate", align="C")


name = input("Name: ")
pdf = PDF()
pdf.add_page()
pdf.image("shirtificate.png", w=185, x=10, y=70)
pdf.set_font("helvetica", size = 20)
pdf.set_text_color(r=255, g=255, b=255)
pdf.cell(-30, 250, f"{name} took CS50", align = "C")
pdf.output("shirtificate.pdf")
