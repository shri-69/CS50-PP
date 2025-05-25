from fpdf import FPDF
name = input("Name: ")
pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.add_page()
pdf.set_font("Helvetica", "B", 24)
pdf.cell(0, 30, "CS50 Shirtificate", ln=True, align="C")


pdf.image("shirtificate.png", x=15, y=60, w=180)


pdf.set_text_color(255, 255, 255)  # white color
pdf.set_font("Helvetica", "B", 20)
pdf.set_y(130)
pdf.cell(0, 10, f"{name} took CS50", align="C")


pdf.output("shirtificate.pdf")
