from reportlab.platypus import BaseDocTemplate, SimpleDocTemplate, Table, Image, TableStyle, Spacer, Paragraph
from reportlab.lib.pagesizes import landscape, letter
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_RIGHT, TA_JUSTIFY


class DMTD_Styles:


    PAGE_HEIGHT = letter[1]
    PAGE_WIDTH = letter[0]
    
    LEFT_RIGHT_MARGIN = .5 * inch
    BODY_WIDTH = PAGE_WIDTH - ( 2 * LEFT_RIGHT_MARGIN)

    # Any images common to all copies of the doc should be placed here


    # Need to ensure that these add up to the available page width in points. 72 points/inch.
    Table_Column_Width_Question = [36,468]
    Table_Column_Width_Answers = [72,360,72]

    #Define colors used in the document. RGB color space.
    Light_Grey = colors.Color(0.8, 0.8, 0.8)
    CPI_Red = colors.Color(164/255, 31/255, 53/255)

    SubSpecTableStyle = TableStyle([
                    ('ALIGN',(0,0),(-1,-1),'LEFT'),
                    ('FONTSIZE', (0,0), (-1,-1), 10),
                    ('FONTNAME', (0,0), (-1,-1), 'Ubuntu'),
                    # ('GRID',(0,0),(-1,-1),0,colors.black),
                    ('TOPPADDING',(0,0),(-1,-1), 1),
                    ('BOTTOMPADDING',(0,0),(-1,-1), 1),
                    ('VALIGN', (0,0),(-1,-1),'MIDDLE')])

    TopSpecTableStyle = TableStyle([
                    ('ALIGN',(0,0),(-1,-1),'LEFT'),
                    ('FONTSIZE', (0,0), (-1,-1), 10),
                    ('FONTNAME', (0,0), (-1,-1), 'Ubuntu'),
                    # ('BOX',(0,0),(-1,-1),0,colors.black),
                    ('RIGHTPADDING',(0,0),(-1,-1), 0),
                    ('LEFTPADDING',(0,0),(-1,-1), 0),
                    ('TOPPADDING',(0,0),(-1,-1), 0),
                    ('BOTTOMPADDING',(0,0),(-1,-1), 0),
                    ('VALIGN', (0,0),(-1,-1),'MIDDLE')])

    TitleRowTableStyle = TableStyle([
                    ('ALIGN',(0,0),(-1,-1),'CENTER'),
                    ('BACKGROUND',(0,0),(-1,-1),Light_Grey),
                    ('FONTSIZE', (0,0), (-1,-1), 12),
                    ('FONTNAME', (0,0), (-1,-1), 'Ubuntu Bold'),
                    # ('GRID',(0,0),(-1,-1),0,colors.black),
                    ('RIGHTPADDING',(0,0),(-1,-1), 3),
                    ('LEFTPADDING',(0,0),(-1,-1), 3),
                    ('TOPPADDING',(0,0),(-1,-1), 2),
                    ('BOTTOMPADDING',(0,0),(-1,-1), 2),
                    ('VALIGN', (0,0),(-1,-1),'MIDDLE')])

    MultilineTableStyle = TableStyle([
                    ('ALIGN',(0,0),(-1,-1),'LEFT'),
                    ('FONTSIZE', (0,0), (-1,-1), 10),
                    ('FONTNAME', (0,0), (-1,-1), 'Ubuntu'),
                    # ('GRID',(0,0),(-1,-1),0,colors.black),
                    ('RIGHTPADDING',(0,0),(-1,-1), 6),
                    ('LEFTPADDING',(0,0),(-1,-1), 6),
                    ('TOPPADDING',(0,0),(-1,-1), 1),
                    ('BOTTOMPADDING',(0,0),(-1,-1), 1),
                    ('VALIGN', (0,0),(-1,-1),'MIDDLE'),
                    ('NOSPLIT', (0,0), (-1,-1))])

    remove_Padding = TableStyle([                    
                    ('RIGHTPADDING',(-1,0),(-1,-1), 0),
                    ('LEFTPADDING',(-1,0),(-1,-1), 0),
                    ('TOPPADDING',(-1,0),(-1,-1), 0),
                    ('BOTTOMPADDING',(-1,0),(-1,-1), 0)])
    
    SpecTableParagraphStyle = ParagraphStyle('normal')
    SpecTableParagraphStyle_Right = ParagraphStyle('normal')

    @classmethod
    def Set_SpecTableParagraphStyle(cls, **kwargs):
        paragraph_properties = ('alignment', 
                                'allowOrphans', 
                                'allowWidows',
                                'backColor',
                                'borderColor',
                                'borderPadding',
                                'borderRadius',
                                'borderWidth',
                                'bulletAnchor',
                                'bulletFontName',
                                'bulletFontSize',
                                'bulletIndent',
                                'embeddedHyphenation',
                                'endDots',
                                'firstLineIndent',
                                'fontName',
                                'fontSize',
                                'hyphenationLang',
                                'justifyBreaks',
                                'justifyLastLine',
                                'leading',
                                'leftIndent',
                                'linkUnderline',
                                'rightIndent',
                                'spaceAfter',
                                'spaceBefore',
                                'spaceShrinkage',
                                'splitLongWords',
                                'strikeGap',
                                'strikeOffset',
                                'strikeWidth',
                                'textTransform',
                                'underlineOffset',
                                'underlineWidth',
                                'uriWasteReduce',
                                'wordWrap')

        for key, value in kwargs.items():
            
            if key in paragraph_properties:
                setattr(cls.SpecTableParagraphStyle, key, value)
            
            else:
                raise NameError('Not A Valid Parameter Name')


    @classmethod
    def Set_SpecTableParagraphStyle_Font(cls,FONTNAME):
        cls.SpecTableParagraphStyle.fontName = FONTNAME

    @classmethod
    def Set_SpecTableParagraphStyle_Title(cls):
        cls.SpecTableParagraphStyle.fontName = 'Ubuntu Bold'
        cls.SpecTableParagraphStyle.fontSize = 12
        cls.SpecTableParagraphStyle.alignment = TA_CENTER

    @classmethod
    def Set_SpecTableParagraphStyle_Body(cls):
        cls.SpecTableParagraphStyle.fontName = 'Helvetica'
        cls.SpecTableParagraphStyle.fontSize = 10
        cls.SpecTableParagraphStyle.alignment = TA_LEFT

    @classmethod
    def Set_SpecTableParagraphStyle_Right(cls):
        cls.SpecTableParagraphStyle_Right.fontName = 'Helvetica'
        cls.SpecTableParagraphStyle_Right.fontSize = 10
        cls.SpecTableParagraphStyle_Right.alignment = TA_RIGHT

    

class doc_properties:

    Title = "PATSA Written Exam"

    pageinfo = "2021 Edition"
    document_number = "Event Num"
    document_revision = "Event Num"