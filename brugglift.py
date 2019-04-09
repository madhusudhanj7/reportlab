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
from reportlab.lib.colors import red, yellow, green
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.graphics.shapes import *

styles=getSampleStyleSheet()
stylesN = styles['Normal']
stylesH =styles['Heading1']
MARGIN_SIZE = 8 * mm
PAGE_SIZE = A4
doc = SimpleDocTemplate("brugglift.pdf", pagesize=letter, leftMargin = MARGIN_SIZE,rightMargin = MARGIN_SIZE,topMargin = 1*MARGIN_SIZE, bottomMargin = 0)
elements=[]
logo = "brugg_logo.png"
logo1 = "brugg.jpg"
product = "stars.jpeg"
bg = "cables.jpg"
s03 = []
im = GNAA(logo, 1.5*inch, 0.5*inch)
s03.append(im)
dataHeader =[[s03]]
t1=Table(dataHeader,colWidths=(190*mm))
t1.setStyle(TableStyle([('ALIGN',(0,0),(-1,-1),'RIGHT'),('VALIGN',(0,0),(-1,-1),'TOP'),]))
elements.append(t1)
pparh1 = elements.append(Paragraph('<para align="LEFT"><b>Eine starke Symbiose</b><br/> <br/>SCX9- das neue Vollstahl-Aufzugseil verbindet geringerer<br/>Dehnung, uberdurchschnittlicher Bruchkraft und Lebendauer des Parallel- <br/>schlag-Aufzugseils mit der Robustheit und der Montagefreundlichkeit des<br/>standard-geschlangenen Aufzugseils<br/> </para>',styles["Normal"]))
elements.append(Spacer(1, 15))
pparh2 = elements.append(Paragraph('<para align="LEFT"><b>A strong symbiosis</b> <br/><br/>SCX9 - the new steel core elevetor ropes combines the advantage of<br/>the parallel-lay elevator rope, which are lower elongation, above-average<br/>breaking strength and service life, with the advantages of the standard lay<br/>elevator rope, which are robustness and ease of installation<br/> </para>',styles["Normal"]))
elements.append(Spacer(1, 50))

P1 = Paragraph('''<para align=left fontSize=38><b><b>S C X 9</b></b> </para>''', styles["BodyText"])

P2 = Paragraph('''<para fontSize=10>DAS VOLLSTAHL-AUFZUGSEIL <br/>
THE STEEL CORE ELEVATOR ROPE</para>''', styles["BodyText"])
elements.append(Spacer(1, 3))

# P= Paragraph('''<para fontSize=12>THE STEEL CORE ELEVATOR ROPE</para>''', styles["BodyText"])
data1 = [[P1]]
data2 = [[P2]]


t2=Table(data1,colWidths=(180*mm))
t2.setStyle(TableStyle([('TEXTFONT', (0, 0), (-1, -1), 'Times-Bold'),('TEXTCOLOR',(0,0),(-1,-1),black),('ALIGN',(0,0),(-1,-1),'RIGHT'),('VALIGN',(0,0),(-1,-1),'TOP')]))
elements.append(t2)

t3=Table(data2,colWidths=(70*mm))
t3.setStyle(TableStyle([('TEXTFONT', (0, 0), (-1, -1), 'Times-Bold'),('TEXTCOLOR',(0,0),(-1,-1),black),('ALIGN',(0,0),(-1,-1),'RIGHT'),('VALIGN',(0,0),(-1,-1),'TOP')]))
elements.append(t3)
img = GNAA(logo1, 9.1*inch, 6*inch)

elements.append(img)
elements.append(Spacer(1, 3))

#for BACKSIDE VIEW

ppar1 = Paragraph('<para  align="LEFT"><b>Vollastahseil, 9 litzen,gensondert verseilt</b> <br/>Fur hochste Anforderungen im Bezug auf BruchKraft<br/>Dehnung und Fahrtenzahl, auch bei erschwerten <br/>montagesitunationen. Empfohlen fur Runderillen mit<br/>einem Unterschnittwinkel < 85.<br/><br/> <b>steel core rope,9 dtrands, seperate lay</b><br/>For highest demandas on breaking force, elongation<br/>and number of trips, also under difficult instalation<br/>condtions. Recommended for round grooves with an <br/>undercut angle of < 85.</para>',styles['Normal'])
parag1 = [[ppar1]]
paragar=Table(parag1,colWidths=(90*mm),rowHeights=(50*mm))
# elements.append(paragar)
tp1 = Paragraph('<para fontSize=7>E-Module</para>',styles['Normal'])
b1 = [[tp1]]
tpl1 = Table(b1)

datatab1 = [
   ['120,000' ],
   ['N/mm2'],
   ]
tab1=Table(datatab1,colWidths=(14*mm),rowHeights=(7*mm))
tab1.setStyle(TableStyle([('TEXTFONT', (0, 0), (-1, -1), 'Times-Bold'),
                        ('BACKGROUND',(0,0),(0,1),colors.lightblue),
                        ('TEXTCOLOR',(0,0),(-1,-1),black),
                        ('ALIGN',(0,0),(-1,-1),'CENTER'),
                        ('FONTSIZE', (0, 0), (0, 1), 7),
                        ('BOTTOMPADDING',(0,0),(0,0),-5),

                        ]))
tp2 = Paragraph('<para fontSize=7 >Elastic<br/> elongation</para>',styles['Normal'])
b2 = [[tp2]]
tpl2 = Table(b2)
datatab2 = [
   ['0.108' ],
   ['%'],
   ]

tab2=Table(datatab2,colWidths=(14*mm),rowHeights=(7*mm))
tab2.setStyle(TableStyle([('TEXTFONT', (0, 0), (-1, -1), 'Times-Bold'),
                        ('BACKGROUND',(0,0),(0,1),colors.lightblue),
                        ('TEXTCOLOR',(0,0),(-1,-1),black),
                        ('ALIGN',(0,0),(-1,-1),'CENTER'),
                        ('FONTSIZE', (0, 0), (0, 1), 7),
                        ('BOTTOMPADDING',(0,0),(0,0),-5),
                        ]))
tp3 = Paragraph('<para fontSize =7>Permenant <br/>elongation</para>',styles['Normal'])
b3  =[[tp3]]
tpl3 = Table(b3)
datatab3 = [
   ['0.16' ],
   ['%'],
   ]
tab3=Table(datatab3,colWidths=(14*mm),rowHeights=(7*mm))
tab3.setStyle(TableStyle([('TEXTFONT', (0, 0), (-1, -1), 'Times-Bold'),
                        ('BACKGROUND',(0,0),(0,1),colors.lightblue),
                        ('TEXTCOLOR',(0,0),(-1,-1),black),
                        ('ALIGN',(0,0),(-1,-1),'CENTER'),
                        ('FONTSIZE', (0, 0), (0, 1), 7),
                        ('BOTTOMPADDING',(0,0),(0,0),-5),

                        ]))

tp4 = Paragraph('<para fontSize=7>Lifting height</para>',styles['Normal'])
b4 = [[tp4]]
tpl4 =Table(b4)
datatab4 = [
   ['<=325' ],
   ['m'],
   ]
tab4=Table(datatab4,colWidths=(14*mm),rowHeights=(7*mm))
tab4.setStyle(TableStyle([('TEXTFONT', (0, 0), (-1, -1), 'Times-Bold'),
                        ('BACKGROUND',(0,0),(0,1),colors.lightblue),
                        ('TEXTCOLOR',(0,0),(-1,-1),black),
                        ('ALIGN',(0,0),(-1,-1),'CENTER'),
                        ('FONTSIZE', (0, 0), (0, 1), 7),
                        ('VALIGN',(1,0),(0,1),'TOP'),
                        ('BOTTOMPADDING',(0,0),(0,0),-5),

                        ('ALIGN',(0,1),(0,0),'CENTER'),
                        ('ALIGN',(0,1),(0,1),'CENTER'),

                        ]))

table5=[[tab1,tab2,tab3,tab4],
        [tpl1,tpl2,tpl3,tpl4]]
tab5 = Table(table5,colWidths=(20*mm),rowHeights=(12*mm))
tab5.setStyle(TableStyle([('TEXTFONT', (0, 0), (-1, -1), 'Times-Bold'),

                        ('TEXTCOLOR',(0,0),(-1,-1),black),
                        ('ALIGN',(0,0),(-1,-1),'CENTER'),
                        ('VALIGN',(1,0),(0,1),'TOP'),
                        ('BOTTOMPADDING',(0,0),(-1,-1),-20),
                        ('ALIGN',(0,1),(-1,-1),'CENTER'),

                        ]))

p = [[paragar,tab5]]
para = Table(p,colWidths=(90*mm),rowHeights=(55*mm))
para.setStyle(TableStyle([('TEXTFONT', (0, 0), (-1, -1), 'Adrianna light italic'),('TEXTCOLOR',(0,0),(-1,-1),black),('VALIGN',(0,0),(-1,-1),'TOP'),('ALIGN',(0,0),(-1,-1),'CENTER')]))
elements.append(para)
prd = GNAA(product, 3*inch, 2*inch)
product = [[prd]]
pic = Table(product,colWidths=(90*mm),rowHeights=(-10*mm))
pic.setStyle(TableStyle([('TEXTFONT', (0, 0), (-1, -1), 'Adrianna light italic'),('TEXTCOLOR',(0,0),(-1,-1),black),('TOPPADDING', (0, 0), (0, 0), -170),('VALIGN',(0,0),(-1,-1),'TOP'),('ALIGN',(0,0),(-1,-1),'CENTER')]))

tp = Paragraph('<para fontSize=6>Further nominal strengths and/or diameters (including imperial dimenstions) on request.<br/>Rope diameter-tolerances according to EN12385-5/ISO 4344</para>',styles['Normal'])
tq = [[tp]]
t6 = Table(tq)

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
mid = [[pic,t5],
        ['',[tq]]]
m = Table(mid)
elements.append(m)

elements.append(Spacer(0.25*inch,0.25*inch))
backg = GNAA(bg,9.25*inch,3.5*inch)
elements.append(backg)

foot= Paragraph('<para align="LEFT" fontsize=7 spaceBefore=12>Ein Unternehemen der Gru0ppe BRUGG<br/>A company of the BRUGG Group</para>',styles['Normal'])
f =  [[foot]]
f0 = Table(f)
elements.append(f0)
elements.append(Spacer(0.3*inch,0.3*inch))

foot1= Paragraph('<para fontsize=7 align="LEFT" spaceBefore=12> Anderungen vorbehalten. Massangaben unverbindlich.<br/>Keine Gewahrleistung fur Druckfehler oder irrtumer.<br/>subject to changes.Nonbinding indication of measures.<br/>No warranty for printing errors of errors.</para>',styles['Normal'])
foot = [[foot1]]
f1 = Table(foot)
foot2= Paragraph('<para  fontsize=10 align="RIGHT">www.brugglifting.com</para>',styles['Normal'])
foot3 = [[foot2]]
f2 = Table(foot3,rowHeights=(65*mm))
footer = [[foot1,foot2]]
f = Table(footer)
elements.append(Spacer(1,12))
elements.append(f)

doc.build(elements)
