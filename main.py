from ebooklib import epub
from fpdf import FPDF
from bs4 import BeautifulSoup
import ebooklib 

def convert_epub_to_pdf(epub_file, pdf_file):

    #! Set book variable equal to the loaded epub file
    #! Both files should be in root directory and sets blank PDF
    book = epub.read_epub(epub_file)
    pdf = FPDF()
    
    #! Add page to PDF
    pdf.add_page()

    #! Extract all text from the EPUB
    for item in book.get_items():
        if item.get_type() == ebooklib.ITEM_DOCUMENT: 
            #! Parse epub contents 
            soup = BeautifulSoup(item.get_content(), 'html.parser')
            text = soup.get_text()

            #? Encode text to ASCII, ignoring characters that cannot be encoded in 'latin-1'
            #todo: This will have to be modified to account for other types of characters 
            text = text.encode('latin-1', 'ignore').decode('latin-1')

            #! Write text to PDF
            pdf.set_font("Arial", size=12)
            pdf.multi_cell(0, 10, text)
    pdf.output(pdf_file)

convert_epub_to_pdf('input.epub', 'output.pdf')
