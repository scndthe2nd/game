"""Print a PDF file from an HTML page, including fillable elements"""
import subprocess
import os
from PyPDF2 import PdfReader, PdfWriter
from PyPDF2.generic import NameObject, NumberObject, DictionaryObject
from utils.html_functions import get_title_from_html

from default_vars import get_default

# Instantiate the PDFPrinter class
  # Update this path

PROCESSOR_PATH = get_default("wkhtmltopdf_path")

def convert_html_to_pdf(input_html='view.html', orientation='portrait'):
    """Convert an HTML file to pdf"""
    # Get the title from the HTML file
    output_pdf_name = get_title_from_html(input_html)
    # Get the user's profile directory
    user_profile_dir = os.path.expanduser('~/Documents/')
    output_dir = os.path.join(user_profile_dir, 'PDFs')
    os.makedirs(output_dir, exist_ok=True)
    output_pdf = os.path.join(output_dir, output_pdf_name)

    # Command to convert HTML to PDF
    command = [PROCESSOR_PATH, '--orientation', orientation, input_html, output_pdf]
    # Run the command
    subprocess.run(command, check=False)
    # Open the generated PDF
    reader = PdfReader(output_pdf)
    writer = PdfWriter()
    for page in reader.pages:
        writer.add_page(page)
        # Check if the page has annotations
        if "/Annots" in page:
            annotations = page["/Annots"]
            for annot in annotations:
                annot_obj = annot.get_object()
                field_type = annot_obj.get("/FT")
                # Highlight text fields and checkboxes
                if field_type == NameObject("/Tx"):
                    if "/MK" not in annot_obj:
                        annot_obj.update({
                            NameObject("/MK"): DictionaryObject()
                        })
                    annot_obj["/MK"].update({
                        NameObject("/BG"): [1, 1, 0]  # Yellow background color
                    })
                elif field_type == NameObject("/Btn"):
                    if "/MK" not in annot_obj:
                        annot_obj.update({
                            NameObject("/MK"): DictionaryObject()
                        })
                    annot_obj["/MK"].update({
                        NameObject("/BG"): [1, 1, 0]  # Yellow background color
                    })
                    # Make checkboxes interactive
                    if "/V" not in annot_obj:
                        annot_obj.update({
                            NameObject("/V"): NameObject("/Off")
                        })
                    if "/AS" not in annot_obj:
                        annot_obj.update({
                            NameObject("/AS"): NameObject("/Off")
                        })
                    annot_obj.update({
                        NameObject("/T"): NameObject("Checkbox"),
                        NameObject("/FT"): NameObject("/Btn"),
                        NameObject("/Ff"): NumberObject(49152)  # Set the checkbox flags
                    })
    # Save the updated PDF with highlighted fields
    with open(output_pdf, "wb") as f_out:
        writer.write(f_out)
    print(f"The PDF with fillable, highlighted fields has been created: {output_pdf}")

    # Open the PDF file
    os.startfile(output_pdf)
