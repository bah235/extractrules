from styles import DMTD_Styles, doc_properties
from reportlab.lib.units import inch


def FirstPage(canvas, doc):
    """This function is used by Reportlab to generate the layout of the
    firstpage and should be thought of as the first page template.

    Args:
        canvas ([Reportlab Canvas Object]): The canvas is the page layout for the first page
        doc ([The Reportlab document Object]): The container for the whole document
    """
    canvas.saveState()
    canvas.setFont("Ubuntu", 16)
    canvas.drawCentredString(
        DMTD_Styles.PAGE_WIDTH / 2.0, DMTD_Styles.PAGE_HEIGHT - 72, doc_properties.Title
    )
    canvas.setFont("Ubuntu", 9)
    canvas.drawString(
        0.5 * inch, 0.5 * inch, "Page 1 / %s" % doc_properties.pageinfo
    )
    # canvas.drawImage(
    #     DMTD_Styles.logo_file,
    #     0.5 * inch,
    #     DMTD_Styles.PAGE_HEIGHT - (1 * inch),
    #     width=2.0 * inch,
    #     height=0.5 * inch,
    #     mask=[0, 0, 0, 0, 0, 0],
    # )
    canvas.restoreState()


def LaterPages(canvas, doc):
    """[summary]

    Args:
        canvas ([Reportlab Canvas Object]): The canvas is the page layout for the first page
        doc ([The Reportlab document Object]): The container for the whole document
    """
    canvas.saveState()
    canvas.setFont("Ubuntu", 9)
    canvas.drawString(
        0.5 * inch,
        0.5 * inch,
        "Page %d  - %s"
        % (
            doc.page,
            doc_properties.pageinfo
        ),
    )
    canvas.restoreState()
