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
from reportlab.pdfgen.canvas import Canvas
from reportlab.graphics.shapes import *
from reportlab.graphics import renderPDF
from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.colors import red, yellow, green, gray, white
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.graphics.shapes import *
from reportlab.platypus import Image
from reportlab.graphics import shapes
from reportlab.graphics.charts.textlabels import Label
from reportlab.graphics import renderPDF, renderPM
from reportlab.graphics.shapes import Drawing
from svglib.svglib import svg2rlg
from reportlab.graphics import renderPDF
from PIL import Image, ImageFilter
from svglib.svglib import svg2rlg
from reportlab.graphics.shapes import Drawing
from reportlab.graphics import renderSVG

styles=getSampleStyleSheet()
stylesN = styles['Normal']
stylesH =styles['Heading1']
c = Canvas("brugglift.pdf")

logo = "brugglifting.svg"
logo1 = "brugg.jpg"
rope = "ropetech.png"
product = "stars.jpeg"
bg = "cables.jpg"
whit = "whity.png"

c.linearGradient(10*mm, 275*mm, 5*mm, 5*mm, (gray, white))

# drawing = svg2rlg(logo)
# renderPDF.draw(drawing, c, 450, 800)

drawing = svg2rlg(logo)
scaleFactor = 1./0.6
drawing.width *= scaleFactor
drawing.height *= scaleFactor
drawing.scale(scaleFactor, scaleFactor)
renderPDF.draw(drawing, c, 405, 795)



textobject = c.beginText()
textobject.setTextOrigin(0.7*inch, 10*inch)
c.setFont('Helvetica-Bold', 11)
c.setFillColorRGB(255,255,255)
textobject.textLines('''Eine starke Symbiose''')
c.drawText(textobject)

textobject = c.beginText()
textobject.setTextOrigin(0.7*inch, 9.7*inch)
c.setFont('Helvetica', 11)
c.setFillColorRGB(255,255,255)
textobject.textLines('''SCX9- das neue Vollstahl-Aufzugseil verbindet geringerer
                        Dehnung, uberdurchschnittlicher Bruchkraft und Lebendauer des Parallel-
                        schlag-Aufzugseils mit der Robustheit und der Montagefreundlichkeit des
                        standard-geschlangenen Aufzugseils''')
c.drawText(textobject)

textobject = c.beginText()
textobject.setTextOrigin(0.7*inch, 8.6*inch)
c.setFont('Helvetica-Bold', 11)
c.setFillColorRGB(0,0,0)
textobject.textLines('''A strong symbiosis''')
c.drawText(textobject)
# c.linearGradient(10*mm, 275*mm, 5*mm, 5*mm, (gray, white))

textobject = c.beginText()
textobject.setTextOrigin(0.7*inch, 8.3*inch)
c.setFont('Helvetica', 11)
c.setFillColorRGB(0,0,0)
textobject.textLines('''SCX9 - the new steel core elevetor ropes combines the advantage of
                        the parallel-lay elevator rope, which are lower elongation, above-average
                        breaking strength and service life, with the advantages of the standard lay
                        elevator rope, which are robustness and ease of installation''')
c.drawText(textobject)

textobject = c.beginText()
textobject.setTextOrigin(0.7*inch, 6*inch)
textobject.setFont('Helvetica-Bold', 49)
c.setFillColorRGB(0,0,0)
textobject.textLines('''S C X 9''')
c.drawText(textobject)

textobject = c.beginText()
textobject.setTextOrigin(3.4*inch, 6.25*inch)
textobject.setFont('Helvetica', 12.5)
c.setFillColorRGB(0,0,0)
textobject.textLines('''DAS VOLLSTAHL-AUFZUGSEIL
                     THE STEEL CORE ELEVATOR ROPE''')
c.drawText(textobject)

c.drawImage(logo1,1,2.5,width=750,height=425,mask='auto')
c.drawInlineImage(rope,45,30,width=100,height=40)
c.showPage()


c.linearGradient(30*mm, 60*mm, 30*mm, 30*mm, (white, grey))
# for box1
# c.setFillGray(0.8)

textobject = c.beginText()
textobject.setTextOrigin(0.5*inch, 11.3*inch)
textobject.setFont('Helvetica-Bold', 12.5)
c.setFillColorRGB(0,0,0)
textobject.textLines('''SCX9 -
                        SCX9 -''')
c.drawText(textobject)

textobject = c.beginText()
textobject.setTextOrigin(1.1*inch, 11.3*inch)
textobject.setFont('Helvetica', 12.5)
c.setFillColorRGB(0,0,0)
textobject.textLines('''DAS VOLLSTAHL-AUFZUGSEIL
                        THE STEEL CORE ELEVATOR ROPE''')
c.drawText(textobject)

drawing = svg2rlg(logo)
scaleFactor = 1./0.7
drawing.width *= scaleFactor
drawing.height *= scaleFactor
drawing.scale(scaleFactor, scaleFactor)
renderPDF.draw(drawing, c, 420, 800)

c.setFillGray(0.6)
c.setStrokeColor(colors.white)
c.rect(3.65*inch,9.5*inch,0.6*inch,0.6*inch, fill=1)
c.setFont("Helvetica-Bold", 7)

c.setFillColor(colors.black)
c.drawString(3.80*inch, 9.8*inch, "120,000")
c.setFont("Helvetica", 5)

c.drawString(3.85*inch, 9.6*inch, "N/mm2")
c.drawString(3.85*inch, 9.3*inch, "E-Modul")
c.drawString(3.85*inch, 9.2*inch, "E-Module")
# for box2

# c.setFillGray(0.87)
c.setFillGray(0.66)
c.rect(4.45*inch,9.5*inch,0.6*inch,0.6*inch, fill=1)
c.setFont("Helvetica-Bold", 7)
c.setFillColor(colors.black)
c.drawString(4.65*inch,9.8*inch, "0.108")
c.setFont("Helvetica", 5)
c.drawString(4.75*inch,9.6*inch, "%")
c.drawString(4.6*inch, 9.4*inch, "elastische")
c.drawString(4.5*inch, 9.3*inch, "Tragseildehnung")
c.drawString(4.65*inch, 9.2*inch, "Elastic")
c.drawString(4.60*inch, 9.1*inch, "elongation")
# for box3

# c.setFillGray(0.93)
c.setFillGray(0.72)
c.rect(5.25*inch,9.5*inch,0.6*inch,0.6*inch, fill=1)
c.setFont("Helvetica-Bold", 7)
c.setFillColor(colors.black)
c.drawString(5.45*inch,9.8*inch, "0.16")
c.setFont("Helvetica", 5)
c.drawString(5.5*inch,9.6*inch, "%")
c.drawString(5.4*inch, 9.4*inch, "elastische")
c.drawString(5.3*inch, 9.3*inch, "Tragseildehnung")
c.drawString(5.40*inch, 9.2*inch, "Permenant")
c.drawString(5.40*inch, 9.1*inch, "elongation")
# for box4

# c.setFillGray(0.95)
c.setFillGray(0.8)
c.rect(6.05*inch,9.5*inch,0.6*inch,0.6*inch, fill=1)
c.setFont("Helvetica-Bold", 7)
c.setFillColor(colors.black)
c.drawString(6.25*inch,9.8*inch, "<325")
c.setFont("Helvetica", 5)

c.drawString(6.35*inch,9.6*inch, "m")
c.drawString(6.15*inch, 9.3*inch, "Lifting height")


textobject = c.beginText()
textobject.setTextOrigin(0.5*inch, 10*inch)
textobject.setFont("Helvetica-Bold", 10)
textobject.setFillColorRGB(0,0,0)
textobject.textLines('''
                    Vollastahseil, 9 litzen,gensondert verseilt''')
c.drawText(textobject)
textobject = c.beginText()

textobject.setTextOrigin(0.5*inch, 9.8*inch)
textobject.setFont("Helvetica", 9)

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
textobject.setTextOrigin(0.5*inch, 8.8*inch)
textobject.setFont("Helvetica", 9)

textobject.textLines('''

                    For highest demandas on breaking force, elongation
                    and number of trips, also under difficult instalation
                    conditions. Recommended for round grooves with an
                    undercut angle of < 85.''')
c.drawText(textobject)
c.drawImage(product,1.2*inch,6.3*inch,width=1.4*inch,height=1.4*inch,mask='auto')
data = [
   ['item-no', 'rope-@', 'rechn./calc',  'min./min.' , 'weight', "construction"],
   ['11666',   '8.0',         '51,1',         '41.9',     '26.3',     '9x19S-IWRC 1570 U sZ(RRL)'],
   ['11668',   '10.0',        '80,2',         '65.8',     '41.3',     '9x19S-IWRC 1570 U sZ(RRL)'],
   ['11669',   '11.0',        '93,3',         '76.5',     '48.0',     '9x19S-IWRC 1570 U sZ(RRL)'],
   ['73107',   '12.7',        '132,0',        '108.3',    '68.0',     '9x21F-IWRC 1570 U sZ(RRL)'],
   ['11671',   '13.0',        '135,4',        '111.0',    '70.7',     '9x21F-IWRC 1570 U sZ(RRL)'],
   ['11674',   '16.0',        '207,8',        '170.4',    '107.2',    '9x25F-IWRC 1570 U sZ(RRL)'],
   ['11675',   '19.0',        '293,6',        '240.7',    '151.3',    '9x25F-IWRC 1570 U sZ(RRL)'],

   ]

t5 =  Table(data,colWidths=18*mm,rowHeights=6*mm)
t5.setStyle(TableStyle([ ('LINEABOVE',(0,1),(-1,1),0.5,colors.black),
                    ('LINEABOVE',(0,1),(-1,-1),0.25,colors.black),
                    ('LINEBELOW',(0,1),(-1,-1),0.25,colors.black),
                    # ('LINEBELOW',(0,1),(-1,3),0.25,colors.black),
                    # ('LINEBELOW',(0,1),(-1,4),0.25,colors.black),
                    # ('LINEBELOW',(0,1),(-1,5),0.25,colors.black),
                    # ('LINEBELOW',(0,1),(-1,6),0.25,colors.black),
                    # ('LINEBELOW',(0,1),(-1,7),0.25,colors.black),
                    ('FONTSIZE', (0, 0), (-1, -1), 6),
                    ('FONTNAME', (0, 0), (1,0), "Helvetica-Bold"),
                    ('FONTNAME', (2, 0), (3,0), "Helvetica-Bold"),
                    ('FONTNAME', (4,0), (5,0), "Helvetica-Bold"),
                    ('ALIGN', (0, 0), (0, 7), 'CENTER'),
                    ('ALIGN', (1, 0), (1, 7), 'CENTER'),
                    ('ALIGN', (2, 0), (-1, 7), 'CENTER'),
                    ('ALIGN', (3, 0), (-1, 7), 'LEFT'),
                    ('ALIGN', (4, 0), (-1, 7), 'LEFT'),
                    ('ALIGN', (5, 0), (-1, 7), 'CENTER'),
                    ('VALIGN', (5, 0), (-1, 7), 'BOTTOM'),
                    ('LEFTPADDING', (1, 1), (-1, 7), 5),
                    ('LEFTPADDING', (2, 0), (-1, 7), -10),
                    ('LEFTPADDING', (3, 0), (-1, 7), -10),
                    ('LEFTPADDING', (4, 0), (-1, 7), -30),
                    ('LEFTPADDING', (5, 0), (-1, 7), -50),
                    ('BACKGROUND', (1,0), (1, 1), '#DCDCDC'),
                    ('BACKGROUND', (1,2), (1, 3), '#DCDCDC'),
                    ('BACKGROUND', (1,4), (1, 5), '#DCDCDC'),
                    ('BACKGROUND', (1,6), (1, 7), '#DCDCDC'),
                    ]))

t5.wrapOn(c, 60, 100)
t5.drawOn(c, 270,450)
textobject1 = c.beginText()
textobject1.setTextOrigin(3.75*inch, 6.1*inch)
c.setFillColor(colors.black)
textobject1.setFont("Helvetica", 7)
textobject1.textLines('''Weitere Nennfestigkeiten und/oder Durchmesser (auch   imperial Masse) auf Anfrage.
                        Seildurchmesser-Toleranzen nach EN12385-5/ISO 4344.''')
c.drawText(textobject1)
textobject = c.beginText()

textobject1 = c.beginText()
textobject1.setTextOrigin(3.75*inch, 5.85*inch)
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


textobject.setTextOrigin(5.9*inch, 0.4*inch)
textobject.moveCursor(14,14)
textobject.setFont("Helvetica", 15)
textobject.setFillColor(colors.white)
textobject.textLines('''
www.brugglifting.com''')
c.drawText(textobject)
c.showPage()

c.save()
