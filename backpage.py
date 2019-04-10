import reportlab

from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import inch
from reportlab.lib.units import cm
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm, mm,inch
from reportlab.lib import colors, utils
from reportlab.platypus import Paragraph, Table, TableStyle, Image, Frame, Spacer, PageBreak, BaseDocTemplate, PageTemplate, SimpleDocTemplate, Flowable
from reportlab.platypus.flowables import HRFlowable
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet, TA_CENTER
from reportlab.graphics import barcode, renderPDF
from reportlab.graphics.shapes import *
from reportlab.platypus.flowables import Image as GNAA
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet, TA_CENTER
from reportlab.lib.colors import yellow, red, black,white,grey
from reportlab.graphics.shapes import Rect
from reportlab.lib import colors
from reportlab.graphics.shapes import *
from reportlab.graphics import renderPDF
from reportlab.graphics.shapes import Drawing

from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import inch
from reportlab.lib.units import cm

from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.colors import red, yellow, green
from reportlab.lib.units import mm




styles=getSampleStyleSheet()
stylesN = styles['Normal']
stylesH =styles['Heading1']
MARGIN_SIZE = 8 * mm
PAGE_SIZE = A4
width, height = A4
styles = getSampleStyleSheet()
styleN = styles["BodyText"]
c = Canvas("gradient.pdf",pagesize=letter)
logo = "brugg_logo.png"
logo1 = "team.jpg"
product = "stars.jpeg"
bg = "cables.jpg"



c.linearGradient(30*mm, 60*mm, 30*mm, 30*mm, (white, grey))


c.setFillGray(0.6)
c.setStrokeColor(colors.white)
c.rect(4.10*inch,9.5*inch,0.6*inch,0.6*inch, fill=1)
# c.linearGradient(100*mm, 100*mm, 0.6*inch, 0.6*inch, (white, grey))
c.setFillColor(colors.black)

c.setFont("Helvetica-Bold", 8)
c.drawString(4.20*inch, 9.8*inch, "120,000")
c.drawString(4.23*inch, 9.6*inch, "N/mm2")
c.setFont("Helvetica", 7)
c.drawString(4.20*inch, 9.3*inch, "E-Modul")
c.drawString(4.20*inch, 9.15*inch, "E-Module")

c.setFillGray(0.66)
c.rect(4.9*inch,9.5*inch,0.6*inch,0.6*inch, fill=1)
c.setFillColor(colors.black)
c.setFont("Helvetica-Bold", 8)
c.drawString(5.05*inch,9.8*inch, "0.108")
c.drawString(5.15*inch,9.6*inch, "%")
c.setFont("Helvetica", 7)
c.drawString(5.0*inch, 9.3*inch, "elastische")
c.drawString(4.85*inch, 9.15*inch, "Tragseildehnung")
c.drawString(5.0*inch, 9.0*inch, "Elastic")
c.drawString(4.95*inch, 8.85*inch, "elongation")

c.setFillGray(0.72)
c.rect(5.7*inch,9.5*inch,0.6*inch,0.6*inch, fill=1)
c.setFillColor(colors.black)
c.setFont("Helvetica-Bold", 8)
c.drawString(5.85*inch,9.8*inch, "0.16")
c.drawString(5.9*inch,9.6*inch, "%")
c.setFont("Helvetica", 7)
c.drawString(5.70*inch, 9.3*inch, "bleibende")
c.drawString(5.64*inch, 9.15*inch, "Tragseildehnung")
c.drawString(5.70*inch, 9.0*inch, "Permenant")
c.drawString(5.70*inch, 8.85*inch, "elongation")

# c.setFillColor(colors.lightblue)
c.setFillGray(0.8)
c.rect(6.5*inch,9.5*inch,0.6*inch,0.6*inch, fill=1)
c.setFillColor(colors.black)
c.setFont("Helvetica-Bold", 8)
c.drawString(6.65*inch,9.8*inch, "<325")
c.drawString(6.7*inch,9.6*inch, "m")
c.setFont("Helvetica", 7)
c.drawString(6.55*inch, 9.3*inch, "Forderhohe")
c.drawString(6.55*inch, 9.15*inch, "Lifting height")

textobject1 = c.beginText()
textobject1.setTextOrigin(0.5*inch, 10*inch)
textobject1.setFont("Helvetica-Bold", 10)
textobject1.textLines('''
                    Vollastahseil, 9 litzen,gensondert verseilt''')
c.drawText(textobject1)
textobject = c.beginText()

textobject.setTextOrigin(0.5*inch, 9.75*inch)
textobject.setFont("Helvetica", 10)

textobject.textLines('''
                    Fur hochste Anforderungen im Bezug auf BruchKraft,
                    Dehnung und Fahrtenzahl, auch bei erschwerten
                    montagesitunationen. Empfohlen fur Runderillen mit
                    einem Unterschnittwinkel < 85.''')
c.drawText(textobject)
textobject = c.beginText()
textobject.setTextOrigin(0.5*inch, 9*inch)
textobject.setFont("Helvetica-Bold", 10)
textobject.textLines('''
                    Steel core rope,9 strands, seperate lay''')
c.drawText(textobject)
textobject = c.beginText()
textobject.setTextOrigin(0.5*inch, 8.75*inch)
textobject.setFont("Helvetica", 10)

textobject.textLines('''

                    For highest demandas on breaking force, elongation
                    and number of trips, also under difficult instalation
                    conditions. Recommended for round grooves with an
                    undercut angle of < 85.''')
c.drawText(textobject)
c.drawImage(product,1*inch,6*inch,width=2*inch,height=2*inch,mask='auto')

data = [
   ['item-no', 'rope-@', 'rechn./calc',  'min./min.' , 'weight', "construction"],
   ['11666',   '8.0',         '51,1',         '41.9',     '26.3',     '9x19S-IWRC 1570 U sZ(RRL)'],
   ['11668',   '10.0',        '80,2',         '65.8',     '41.3',
    '9x19S-IWRC 1570 U sZ(RRL)'],
   ['11669',   '11.0',        '93,3',         '76.5',     '48.0',     '9x19S-IWRC 1570 U sZ(RRL)'],
   ['73107',   '12.7',        '132,0',        '108.3',    '68.0',     '9x21F-IWRC 1570 U sZ(RRL)'],
   ['11671',   '13.0',        '135,4',        '111.0',    '70.7',     '9x21F-IWRC 1570 U sZ(RRL)'],
   ['11674',   '16.0',        '207,8',        '170.4',    '107.2',    '9x25F-IWRC 1570 U sZ(RRL)'],
   ['11675',   '19.0',        '293,6',        '240.7',    '151.3',    '9x25F-IWRC 1570 U sZ(RRL)'],

   ]

t5 =  Table(data, colWidths=(17*mm))
t5.setStyle(TableStyle([ ('LINEABOVE',(0,1),(-1,1),0.5,colors.black),
                    ('LINEABOVE',(0,1),(-1,1),0.5,colors.black),
                    ('LINEBELOW',(0,1),(-1,2),0.5,colors.black),
                    ('LINEBELOW',(0,1),(-1,3),0.5,colors.black),
                    ('LINEBELOW',(0,1),(-1,4),0.5,colors.black),
                    ('LINEBELOW',(0,1),(-1,5),0.5,colors.black),
                    ('LINEBELOW',(0,1),(-1,6),0.5,colors.black),
                    ('LINEBELOW',(0,1),(-1,7),0.5,colors.black),
                    ('FONTSIZE', (0, 0), (0, 7), 6),
                    ('FONTSIZE', (0, 0), (1, 7), 6),
                    ('FONTSIZE', (0, 0), (2, 7), 6),
                    ('FONTSIZE', (0, 0), (3, 7), 6),
                    ('FONTSIZE', (0, 0), (4, 7), 6),
                    ('FONTSIZE', (0, 0), (5, 7), 6),
                    ('ALIGN', (0, 0), (0, 7), 'CENTER'),
                    ('ALIGN', (1, 0), (0, 7), 'CENTER'),
                    ('ALIGN', (2, 0), (0, 7), 'CENTER'),
                    ('ALIGN', (3, 0), (0, 7), 'CENTER'),
                    ('ALIGN', (4, 0), (0, 7), 'CENTER'),
                    ('ALIGN', (5, 0), (0, 7), 'CENTER'),
                    ('LEFTPADDING', (0, 0), (0, 7), 0),
                    ('LEFTPADDING', (1, 0), (1, 7), -5),
                    ('LEFTPADDING', (2, 0), (2, 7), -20),
                    ('LEFTPADDING', (3, 0), (3, 7), -30),
                    ('LEFTPADDING', (4, 0), (4, 7), -30),
                    ('LEFTPADDING', (5, 0), (5, 7), -40),
                    ]))
t5.wrapOn(c, 100, 100)
t5.drawOn(c, 290, 450)

textobject1 = c.beginText()
textobject1.setTextOrigin(4*inch, 6.1*inch)
textobject1.setFont("Helvetica", 7)
textobject1.textLines('''Weitere Nennfestigkeiten und/oder Durchmesser (auch   imperial Masse) auf Anfrage.
                        Seildurchmesser-Toleranzen nach EN12385-5/ISO 4344.''')
c.drawText(textobject1)
textobject = c.beginText()

textobject1 = c.beginText()
textobject1.setTextOrigin(4*inch, 5.85*inch)
textobject1.setFont("Helvetica", 7)
textobject1.textLines('''
                    Further nominal strengths and/or diameters (including imperial dimenstions) on request.
                    Rope diameter-tolerances according to EN12385-5/ISO 4344''')
c.drawText(textobject1)
textobject = c.beginText()

c.drawImage(bg,0*inch,1.5*inch,width=9*inch,height=4*inch,mask=None)

textobject = c.beginText()
textobject.setTextOrigin(0.3*inch, 1.2*inch)
textobject.setFont("Helvetica", 7)
c.setFillColorRGB(255,255,255)
textobject.textLines('''
                    Ein Unternehemen der Gruppe BRUGG''')
c.drawText(textobject)

textobject = c.beginText()
textobject.setTextOrigin(0.3*inch, 1.08*inch)
textobject.setFont("Helvetica", 7)
c.setFillColorRGB(0,0,0)
textobject.textLines('''
                    A company of the BRUGG Group''')
c.drawText(textobject)

# c.linearGradient(10*mm, 275*mm, 5*mm, 5*mm, (gray, white))

textobject = c.beginText()
textobject.setTextOrigin(0.3*inch, 0.6*inch)
textobject.setFont("Helvetica", 7)
c.setFillColorRGB(255,255,255)
textobject.textLines('''
                    Anderungen vorbehalten. Massangaben unverbindlich.
                    Keine Gewahrleistung fur Druckfehler oder irrtumer.''')
c.drawText(textobject)

textobject = c.beginText()
textobject.setTextOrigin(0.3*inch, 0.35*inch)
textobject.setFont("Helvetica", 7)
c.setFillColorRGB(0,0,0)
textobject.textLines('''Subject to changes.Nonbinding indication of measures.
                        No warranty for printing errors of errors.''')
c.drawText(textobject)


textobject.setTextOrigin(6*inch, 0.4*inch)
textobject.moveCursor(14,14)
textobject.setFont("Helvetica", 15)
textobject.textLines('''
www.brugglifting.com''')
c.drawText(textobject)
c.showPage()

c.save()
