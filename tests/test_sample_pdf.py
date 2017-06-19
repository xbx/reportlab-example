import unittest
import os
from io import BytesIO
from os.path import abspath, dirname
from reportlab.lib.colors import HexColor
from reportlab.lib.enums import TA_RIGHT
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch, cm, mm
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, BaseDocTemplate, Paragraph, Image, Spacer


COL_SORT = [{"headerName": "name",
             "field": "name",
             "width": 1000,}]

def get_pdf():
    # setup PDF template
    buffer = BytesIO()
    side_margin = 12
    col_widths = [row['width'] for row in COL_SORT]
    page_width = sum(col_widths) + side_margin * 3
    pdf = SimpleDocTemplate(buffer, pagesize=(page_width, 8.5 * inch), rightMargin=side_margin, leftMargin=side_margin,
                            topMargin=side_margin, bottomMargin=side_margin)
    elements = []

    # logo
    parent_dir = dirname(dirname(abspath(__file__)))
    logo_path = os.path.join(parent_dir, 'statics', 'nci-logo.gif')
    with open(logo_path, 'rb') as image_fd:
      logo = Image(image_fd)
    logo.hAlign = 'LEFT'

    heading_style = ParagraphStyle(name='heading', fontSize=16, leading=20, spaceAfter=0,
                                 textColor=HexColor('#ffffff'), backColor=HexColor('#465a81'))
    heading_right_style = ParagraphStyle(name='heading', fontSize=16, leading=20, spaceAfter=0,
                                       textColor=HexColor('#ffffff'), backColor=HexColor('#465a81'),
                                       alignment=TA_RIGHT)
    logo_tbl = Table([[logo]], colWidths=sum(col_widths))
    logo_tbl.hAlign = 'LEFT'
    logo_tbl.setStyle(TableStyle([('BACKGROUND', (0, 0), (-1, -1), HexColor('#B90002'))]))
    elements.append(logo_tbl)

    # build PDF
    pdf.build(elements)
    pdf_string = buffer.getvalue()
    buffer.close()

class TestPDF(unittest.TestCase):
    def test_pdf(self):
        get_pdf()
