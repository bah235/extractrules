from reportlab.platypus import Table, Paragraph
from styles import DMTD_Styles



def QuestionRow(num, question):
    table_row = None

    DMTD_Styles.Set_SpecTableParagraphStyle_Body()

    table_row = Table(
        [
            [
                Paragraph(f"{num}. ", DMTD_Styles.SpecTableParagraphStyle_Right),
                Paragraph(question, DMTD_Styles.SpecTableParagraphStyle)
            ]
        ],
        DMTD_Styles.Table_Column_Width_Question,
    )
    table_row.setStyle(DMTD_Styles.SubSpecTableStyle)

    return table_row



def AnswerRow(choice, answer):
    table_row = None

    DMTD_Styles.Set_SpecTableParagraphStyle_Body()
    DMTD_Styles.Set_SpecTableParagraphStyle_Right()

    table_row = Table(
        [
            [
                Paragraph(choice, DMTD_Styles.SpecTableParagraphStyle_Right),
                Paragraph(answer, DMTD_Styles.SpecTableParagraphStyle)
            ]
        ],
        DMTD_Styles.Table_Column_Width_Answers[0:2],
    )
    table_row.setStyle(DMTD_Styles.SubSpecTableStyle)

    return table_row


def CorrectRow(choice, answer):
    table_row = None

    DMTD_Styles.Set_SpecTableParagraphStyle_Body()
    DMTD_Styles.Set_SpecTableParagraphStyle_Right()

    table_row = Table(
        [
            [
                Paragraph(choice, DMTD_Styles.SpecTableParagraphStyle_Right),
                Paragraph(answer, DMTD_Styles.SpecTableParagraphStyle)
            ]
        ],
        DMTD_Styles.Table_Column_Width_Answers[0:2],
    )
    table_row.setStyle(DMTD_Styles.TitleRowTableStyle)

    return table_row


def IntegrateQuestions(num, question, a, b, c, d, correct, answers):

    table_row = None

    rows = []

    rows.append([QuestionRow(num, question)])
    rows.append([AnswerRow('(A.)', a)])
    rows.append([AnswerRow('(B.)', b)])
    rows.append([AnswerRow('(C.)', c)])
    rows.append([AnswerRow('(D.)', d)])
    if answers == True:
        rows.append([CorrectRow('Correct', correct)])

    DMTD_Styles.Set_SpecTableParagraphStyle_Body()

    table_row = Table(rows, [504,])

    table_row.setStyle(DMTD_Styles.MultilineTableStyle)

    # Remove the excess cell padding from the embedded sub table
    table_row.setStyle(DMTD_Styles.remove_Padding)

    return table_row


