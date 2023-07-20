"""
Title: Problemset_8 - CS50 Shirtificate

Author: Emely Benke

Created: 2023-07-19

Version: 0.1

Summary:
Suppose that you’d like to implement a CS50 “shirtificate,”
a PDF with an image of an I took CS50 t-shirt,
shirtificate.png, customized with a user’s own name.

In a file called shirtificate.py, implement a program that
prompts the user for their name and outputs, using fpdf2,
a CS50 shirtificate in a file called shirtificate.pdf
similar to this one for John Harvard, with these specifications:
--> https://cs50.harvard.edu/python/2022/psets/8/shirtificate/jharvard.png
The orientation of the PDF should be Portrait.
The format of the PDF should be A4, which is 210mm wide by 297mm tall.
The top of the PDF should say “CS50 Shirtificate” as text, centered horizontally.
The shirt’s image should be centered horizontally.
The user’s name should be on top of the shirt, in white text.
All other details we leave to you.
You’re even welcome to add borders, colors, and lines.
Your shirtificate needn’t match John Harvard’s precisely.
And no need to wrap long names across multiple lines.

Before writing any code, do read through fpdf2’s tutorial to learn how to use it.
Then skim fpdf2’s API (application programming interface)
to see all of its functions and parameters therefor.

No need to submit any PDFs with your code. But, if you would like,
you’re welcome (but not expected) to share a shirtificate
with your name on it in any of CS50’s communities!

Hints
Note that fpdf2 comes with a class called FPDF,
which has quite a few methods,
per "pyfpdf.github.io/fpdf2/fpdf/#fpdf.FPDF"
You can install it with: --> pip install fpdf2
Note that you can extend FPDF and instantiate your own subclass
thereof in order to add a header to every page of a PDF,
per "pyfpdf.github.io/fpdf2/Tutorial.html#tuto-2-header-footer-page-break-and-image"
Or you can add it as text yourself.
Note that you can disable automatic page breaks,
which might otherwise cause your PDF to overflow from one page to two,
with set_auto_page_break, per "pyfpdf.github.io/fpdf2/Margins.html"
Note that a cell’s height can be negative, to move it upward.
You can open shirtificate.pdf, once outputted, by clicking it in VS Code’s file explorer.


Here’s how to test your code manually:

Run your program with shirtificate.py.
Make sure your program prompts you for a name.
Enter your own name and press Enter.
Your program should create a file, shirtificate.pdf,
containing the name you entered as input
overlaid on a rendering of shirtificate.png.
Try a few other names for good measure, too!
"""
# Import FPDF-Library for PDF generation
<<<<<<< HEAD
from fpdf import FPDF   
import datetime                                                 
=======
from fpdf import FPDF

>>>>>>> 19c1166de3d30c968abb6d2b5ecd5340ccde565a

class Shirtificate:
    def __init__(self, name):
        self.name = name
        self.generate()
<<<<<<< HEAD
    
=======

>>>>>>> 19c1166de3d30c968abb6d2b5ecd5340ccde565a
    @classmethod
    def get_name(cls):
        """Prompt a name from the user"""
        name = input("Name: ").strip()
        return cls(name)

    def generate(self) -> None:
        """Generate a personal "Shirtificate" for the given name and save it as PDF."""
        # create a pdf object
        pdf = FPDF(orientation="portrait", format="A4")
        # add a blank page to the pdf
        pdf.add_page()
        # disable automatic page breaks
        pdf.set_auto_page_break(auto=False, margin=0)
<<<<<<< HEAD
        
=======

>>>>>>> 19c1166de3d30c968abb6d2b5ecd5340ccde565a
        # set required text properties
        pdf.set_font("Helvetica", "B", 50)
        title: str = "CS50 Shirtificate"
        # write the title on the documents top
<<<<<<< HEAD
        pdf.cell(0, 50, txt=title, align='C')
        pdf.ln()
        
        # load the shirt image into the page
        pdf.image("shirtificate.png", x=15, y=(297/4), w=180)
        
        # write the personal shirt-print on the image 
=======
        pdf.cell(0, 50, txt=title, align="C")
        pdf.ln()

        # load the shirt image into the page
        pdf.image("shirtificate.png", x=15, y=(297 / 4), w=180)

        # write the personal shirt-print on the image
>>>>>>> 19c1166de3d30c968abb6d2b5ecd5340ccde565a
        pdf.set_font("Helvetica", "B", size=20)
        pdf.set_text_color(255, 255, 255)
        personal_print = f"{self.name} took CS50"
        pdf.cell(0, 150, align="C", txt=personal_print)
        pdf.ln()
<<<<<<< HEAD
        
        # save the created pdf document
        pdf.output("shirtificate.pdf")
        
        
def main() -> None:
    Shirtificate.get_name()
    
    
if __name__ == '__main__':
    main()
=======

        # save the created pdf document
        pdf.output("shirtificate.pdf")


def main() -> None:
    Shirtificate.get_name()


if __name__ == "__main__":
    main()
>>>>>>> 19c1166de3d30c968abb6d2b5ecd5340ccde565a
