from fpdf import FPDF

def main():
    t_shirt(input('Name: ').strip().capitalize())

def t_shirt(name):
    pdf = FPDF(orientation="p", unit = 'mm', format="A4")
    pdf.add_page()
    pdf.set_font("Helvetica", style ='B', size = 18)
    pdf.cell(text="CS50 Shirtificate", new_x='LMARGIN', new_y='NEXT', center = True, align="C")
    pdf.image("shirtificate.png", h=pdf.eph/2.2, w=pdf.epw/2, x=pdf.epw/3.3, keep_aspect_ratio=True)
    pdf.set_font("Helvetica", style ='B', size = 12)
    pdf.set_text_color(255, 255, 255)
    pdf.cell(0,-150,text=f"{name} Took CS50", center = True, align="C")
    pdf.output("shirtificate.pdf")

if __name__ == '__main__':
    main()