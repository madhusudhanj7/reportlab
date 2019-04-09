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

styles=getSampleStyleSheet()
stylesN = styles['Normal']
stylesH =styles['Heading1']
c = Canvas("brugglift.pdf")

logo = "brugg_logo.png"
logo1 = "brugg.jpg"
product = "stars.jpeg"
bg = "cables.jpg"
whit = "whity.png"

c.linearGradient(10*mm, 275*mm, 5*mm, 5*mm, (gray, white))

c.drawImage(logo,450,755,width=120,height=60,mask='auto')


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

c.drawImage(whit,390,10,width=800,height=0.2,mask='auto')
c.drawImage(logo1,1,2.5,width=750,height=425,mask='auto')

c.showPage()

c.save()
