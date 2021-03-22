from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
import reportlab.rl_config
import os


class FontNameNotFoundError(Exception):
    pass


# Suppress error related to missing characters in the font set
reportlab.rl_config.warnOnMissingFontGlyphs = 0


def register_type1_font():
    """This function is a maintenence function that registers new Type 1 font for PDF use
    This only need be run on new installations and when installing new fonts. Does not need to be
    run every time a program starts up. This modifies the ReportLab installation."""

    # Define the location of the font to be registered
    folder = os.path.dirname(reportlab.__file__) + os.sep + "fonts"
    afmFile = os.path.join(folder, "DarkGardenMK.afm")
    pfbFile = os.path.join(folder, "DarkGardenMK.pfb")
    justFace = pdfmetrics.EmbeddedType1Face(afmFile, pfbFile)
    faceName = "DarkGardenMK"
    pdfmetrics.registerTypeFace(justFace)
    justFont = pdfmetrics.Font("DarkGardenMK", faceName, "WinAnsiEncoding")
    pdfmetrics.registerFont(justFont)


def register_true_type_font():
    """This function is a maintenence function that registers new True Type Font for PDF use
    This only need be run on new installations and when installing new fonts. Does not need to be
    run every time a program starts up. This modifies the ReportLab installation."""

    pdfmetrics.registerFont(TTFont("Vera", "Vera.ttf"))
    pdfmetrics.registerFont(TTFont("VeraBd", "VeraBd.ttf"))
    pdfmetrics.registerFont(TTFont("VeraIt", "VeraIt.ttf"))
    pdfmetrics.registerFont(TTFont("VeraBI", "VeraBI.ttf"))

    pdfmetrics.registerFont(TTFont("Ubuntu", "Ubuntu-R.ttf"))
    pdfmetrics.registerFont(TTFont("Ubuntu Italic", "Ubuntu-RI.ttf"))
    pdfmetrics.registerFont(TTFont("Ubuntu Bold", "Ubuntu-B.ttf"))
    pdfmetrics.registerFont(TTFont("Ubuntu Bold Italic", "Ubuntu-BI.ttf"))

    pdfmetrics.registerFont(TTFont("Ubuntu Condensed", "Ubuntu-C.ttf"))
    pdfmetrics.registerFont(TTFont("Ubuntu Light", "Ubuntu-L.ttf"))
    pdfmetrics.registerFont(TTFont("Ubuntu Light Italic", "Ubuntu-LI.ttf"))
    pdfmetrics.registerFont(TTFont("Ubuntu Medium", "Ubuntu-M.ttf"))
    pdfmetrics.registerFont(TTFont("Ubuntu Medium Italic", "Ubuntu-MI.ttf"))
    pdfmetrics.registerFont(TTFont("Ubuntu Thin", "Ubuntu-Th.ttf"))

    pdfmetrics.registerFont(TTFont("Ubuntu Monospace Bold", "UbuntuMono-B.ttf"))
    pdfmetrics.registerFont(TTFont("Ubuntu Monospace Bold Italic", "UbuntuMono-BI.ttf"))
    pdfmetrics.registerFont(TTFont("Ubuntu Monospace", "UbuntuMono-R.ttf"))
    pdfmetrics.registerFont(TTFont("Ubuntu Monospace Italic", "UbuntuMono-RI.ttf"))

    pdfmetrics.registerFontFamily(
        "Vera", normal="Vera", bold="VeraBd", italic="VeraIt", boldItalic="VeraBI"
    )
    pdfmetrics.registerFontFamily(
        "Ubuntu Monospace",
        normal="Ubuntu Monospace",
        bold="Ubuntu Monospace Bold",
        italic="Ubuntu Monospace Italic",
        boldItalic="Ubuntu Monospace Bold Italic",
    )
    pdfmetrics.registerFontFamily(
        "Ubuntu",
        normal="Ubuntu",
        bold="Ubuntu Bold",
        italic="Ubuntu Italic",
        boldItalic="Ubuntu Bold Italic",
    )
    pdfmetrics.registerFontFamily(
        "Ubuntu Condensed",
        normal="Ubuntu Condensed",
        bold="Ubuntu Condensed",
        italic="Ubuntu Condensed",
        boldItalic="Ubuntu Condensed",
    )
    pdfmetrics.registerFontFamily(
        "Ubuntu Light",
        normal="Ubuntu Light",
        bold="Ubuntu Light",
        italic="Ubuntu Light Italic",
        boldItalic="Ubuntu Light Italic",
    )
    pdfmetrics.registerFontFamily(
        "Ubuntu Medium",
        normal="Ubuntu Medium",
        bold="Ubuntu Medium",
        italic="Ubuntu Medium Italic",
        boldItalic="Ubuntu Medium Italic",
    )
    pdfmetrics.registerFontFamily(
        "Ubuntu Thin",
        normal="Ubuntu Thin",
        bold="Ubuntu Thin",
        italic="Ubuntu Thin",
        boldItalic="Ubuntu Thin",
    )


def print_character_map(font):
    """ This Utility prints a charactermap for a given font."""

    from reportlab.lib.units import inch
    from reportlab.platypus import SimpleDocTemplate, Spacer, Paragraph
    from reportlab.lib.styles import getSampleStyleSheet
    from build_pages import FirstPage, LaterPages
    from reportlab.lib.pagesizes import letter
    from styles import DMTD_Styles

    register_true_type_font()
    styles = getSampleStyleSheet()
    doc = SimpleDocTemplate((font + ' Character Map.pdf'), pagesize=letter)    
    Story = [Spacer(1,2*inch)]    
    style = styles["Normal"] 

    DMTD_Styles.Set_SpecTableParagraphStyle_Font("Helvetica")

    for i in range(255):
        text = 'Character ' + str(i) + ' is ' + chr(i) 

        
        p = Paragraph(text, DMTD_Styles.SpecTableParagraphStyle)
        Story.append(p)
        Story.append(Spacer(1,0.05*inch))


    doc.build(Story, onFirstPage=FirstPage, onLaterPages=LaterPages)

