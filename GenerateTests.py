# Imports from the Reportlab library
from reportlab.lib.pagesizes import landscape, letter
from reportlab.platypus import SimpleDocTemplate, Table, Image, TableStyle, Spacer, Paragraph, PageBreak
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.rl_config import defaultPageSize
from reportlab.lib import colors

# This module's imports
from font_utils import register_true_type_font
from styles import DMTD_Styles, doc_properties
from build_pages import FirstPage, LaterPages
from build_tables import IntegrateQuestions
from questions import questions


def make_test(exam):

    # Set up custom fonts
    register_true_type_font()

    answers = False


    # Set up Doc properties
    styles = getSampleStyleSheet()
    
    if answers == True:
        doc = SimpleDocTemplate(f"exams/export/2021 {exam.name} ANSWERS.pdf",pagesize=letter)  
    else:
        doc = SimpleDocTemplate(f"exams/export/2021 {exam.name} Test.pdf",pagesize=letter)   

    doc_properties.Title = f"2021 {exam.name} Written Test"
    doc_properties.pageinfo = f"2021 {exam.name} Written Test"

    Story = [Spacer(1,.5*inch)]    
    style = styles["Normal"]   

    doc.leftMargin = 0.75 * inch
    doc.rightMargin = 0.75 * inch
    doc.title = '2021 State Conference Test'
    doc.auther = 'Pennsylvania TSA'

    for num, question, a, b, c, d, correct in zip(exam.numbers, exam.question, exam.choice_a, exam.choice_b, exam.choice_c, exam.choice_d, exam.correct):
        Story.append(IntegrateQuestions(num, question, a, b, c, d, correct, answers))
        Story.append(Spacer(0, 0.25*inch))

    # Append post-table text, if any
    Story.append(Spacer(0, 0.2*inch))  
    post_text = "This is the end of the test. Please submit your answer sheet."        
    p = Paragraph(post_text, style)
    Story.append(p)        

    # Finally, generate and save the PDF
    doc.build(Story, onFirstPage=FirstPage, onLaterPages=LaterPages)


def main():
    MS_ChapterTeam = questions('MS Chapter Team', range(7,12), 12, 50)
    MS_ChapterTeam.import_csv(f"exams/CSV/{MS_ChapterTeam.name}.csv")
    make_test(MS_ChapterTeam)


    MS_Coding = questions('MS Coding', range(17,27), 27, 50)
    MS_Coding.import_csv(f"exams/CSV/{MS_Coding.name}.csv")
    make_test(MS_Coding)


    MS_Cybersecurity = questions('MS Cybersecurity', range(32,39), 39, 60)
    MS_Cybersecurity.import_csv(f"exams/CSV/{MS_Cybersecurity.name}.csv")
    make_test(MS_Cybersecurity)
    

    MS_Electrical = questions('MS Electrical Applications', range(42,49), 49, 50)
    MS_Electrical.import_csv(f"exams/CSV/{MS_Electrical.name}.csv")
    make_test(MS_Electrical)


    MS_Forensic = questions('MS Forensic Science', range(52,57), 57, 50)
    MS_Forensic.import_csv(f"exams/CSV/{MS_Forensic.name}.csv")
    make_test(MS_Forensic)
    

    MS_FIT = questions('MS FIT', range(64,72), 72, 60)
    MS_FIT.import_csv(f"exams/CSV/{MS_FIT.name}.csv")
    make_test(MS_FIT)
    

    MS_Techbowl = questions('MS Techbowl', range(79,85), 85, 50)
    MS_Techbowl.import_csv(f"exams/CSV/{MS_Techbowl.name}.csv")
    make_test(MS_Techbowl)
    

    HS_ChapterTeam = questions('HS Chapter Team', range(96,102), 102, 50)
    HS_ChapterTeam.import_csv(f"exams/CSV/{HS_ChapterTeam.name}.csv")
    make_test(HS_ChapterTeam)
    

    HS_Forensic = questions('HS Forensic Science', range(128,134), 134, 50)
    HS_Forensic.import_csv(f"exams/CSV/{HS_Forensic.name}.csv")
    make_test(HS_Forensic)
    

    HS_IT = questions('HS IT Fundamentals', range(141,148), 148, 50)
    HS_IT.import_csv(f"exams/CSV/{HS_IT.name}.csv")
    make_test(HS_IT)
    

    HS_Techbowl = questions('HS Techbowl', range(156,163), 163, 50)
    HS_Techbowl.import_csv(f"exams/CSV/{HS_Techbowl.name}.csv")
    make_test(HS_Techbowl)
    

    HS_Troubleshooting = questions('HS Troubleshooting', range(156,163), 163, 50)
    HS_Troubleshooting.import_csv(f"exams/CSV/{HS_Troubleshooting.name}.csv")
    make_test(HS_Troubleshooting)









# Run in script mode
if __name__ == '__main__':
    main()