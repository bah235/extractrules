import re
import PyPDF2
import pandas as pd
from log import pdf_log


class questions:

    mult_pattern = r"(\d+)\.\s+(.+)\s+a\.\s+(.+)\s+b\.\s+(.+)\s+c\.\s+(.+)\s+d\.\s+(.+)"
    answer_pattern = r"(\d+)\.\s+([ABCD])"


    def __init__(self, name, question_pages, answer_pages, num):

        self.name = name
        self.numbers = [None] * num
        self.question = [None] * num
        self.choice_a = [None] * num
        self.choice_b = [None] * num
        self.choice_c = [None] * num
        self.choice_d = [None] * num
        self.correct = [None] * num
        self.image = [None] * num
        self.question_pages = question_pages
        self.answer_pages = answer_pages

    def import_csv(self, file):
        
        df = pd.read_csv(file)
        self.numbers = df['num'].tolist()
        self.question = df['question'].tolist()
        self.choice_a = df['choice_a'].tolist()
        self.choice_b = df['choice_b'].tolist()
        self.choice_c = df['choice_c'].tolist()
        self.choice_d = df['choice_d'].tolist()
        self.correct = df['choice_correct'].tolist()


    def export(self):
        
        df = pd.DataFrame( {'num' : self.numbers, 
                            'question' : self.question, 
                            'choice_a' : self.choice_a,
                            'choice_b' : self.choice_b,
                            'choice_c' : self.choice_c,
                            'choice_d' : self.choice_d,
                            'choice_correct' : self.correct } )

        print(df)
        df.to_csv(f"exams/{self.name}.csv")


    def generate_image_hash(self):
        pass


    def insert_answer(self, number, ans):    
        num = int(number)
        if self.correct[num-1] == None:
            self.correct[num-1] = ans
            # pdf_log(f"In {self.name} answer {num} was inserted", 'OK')
        else:
            pdf_log(f"In {self.name} answer {num} has shown up twice", 'FAIL')


    def insert_question(self, number, question, a, b, c, d):        
        num = int(number)
        if self.numbers[num-1] == None:
            self.numbers[num-1] = num
            self.question[num-1] = question
            self.choice_a[num-1] = a
            self.choice_b[num-1] = b
            self.choice_c[num-1] = c
            self.choice_d[num-1] = d
            # pdf_log(f"In {self.name} question {number} was inserted", 'OK')
        else:
            pdf_log(f"In {self.name} question {number} has shown up twice", 'FAIL')


    def scan_pdf(self):
        for pages in self.question_pages:
            pageObj=pdfReader.getPage(pages)

            file1 = open(f"exams/{self.name}-raw.txt","a")  
            file1.writelines(pageObj.extractText()) 
            file1.close()


    def scan_multichoice(self):

        with open (f"exams/{self.name}.txt", "r") as myfile:
            data=myfile.read()    

        previous = 0

        for match in re.finditer(self.mult_pattern, data):
            self.insert_question(match.group(1),match.group(2),match.group(3),match.group(4),match.group(5),match.group(6))

            if int(match.group(1)) != (previous + 1):
                pdf_log(f"In {self.name} question {int(match.group(1))-1} skipped", 'FAIL')

            previous = int(match.group(1))


    def scan_answers(self):
        pageObj=pdfReader.getPage(self.answer_pages)

        for match in re.finditer(self.answer_pattern, pageObj.extractText()):
            self.insert_answer(match.group(1),match.group(2))


def main():
        
    import PyPDF2
    pdfFileObj=open("CRAM.pdf", "rb")
    pdfReader=PyPDF2.PdfFileReader(pdfFileObj)
    pdfReader.numPages

    MS_ChapterTeam = questions('MS Chapter Team', range(7,12), 12, 50)
    MS_ChapterTeam.scan_multichoice()
    MS_ChapterTeam.scan_answers()
    MS_ChapterTeam.export()

    MS_Coding = questions('MS Coding', range(17,27), 27, 50)
    MS_Coding.scan_multichoice()
    MS_Coding.scan_answers()
    MS_Coding.export()

    MS_Cybersecurity = questions('MS Cybersecurity', range(32,39), 39, 60)
    MS_Cybersecurity.scan_multichoice()
    MS_Cybersecurity.scan_answers()
    MS_Cybersecurity.export()

    MS_Electrical = questions('MS Electrical Applications', range(42,49), 49, 50)
    MS_Electrical.scan_multichoice()
    MS_Electrical.scan_answers()
    MS_Electrical.export()

    MS_Forensic = questions('MS Forensic Science', range(52,57), 57, 50)
    MS_Forensic.scan_multichoice()
    MS_Forensic.scan_answers()
    MS_Forensic.export()

    MS_FIT = questions('MS FIT', range(64,72), 72, 60)
    MS_FIT.scan_multichoice()
    MS_FIT.scan_answers()
    MS_FIT.export()

    MS_Techbowl = questions('MS Techbowl', range(79,85), 85, 50)
    MS_Techbowl.scan_multichoice()
    MS_Techbowl.scan_answers()
    MS_Techbowl.export()


    HS_ChapterTeam = questions('HS Chapter Team', range(96,102), 102, 50)
    HS_ChapterTeam.scan_multichoice()
    HS_ChapterTeam.scan_answers()
    HS_ChapterTeam.export()

    HS_Forensic = questions('HS Forensic Science', range(128,134), 134, 50)
    HS_Forensic.scan_multichoice()
    HS_Forensic.scan_answers()
    HS_Forensic.export()

    HS_IT = questions('HS IT Fundamentals', range(141,148), 148, 50)
    HS_IT.scan_multichoice()
    HS_IT.scan_answers()
    HS_IT.export()

    HS_Techbowl = questions('HS Techbowl', range(156,163), 163, 50)
    HS_Techbowl.scan_multichoice()
    HS_Techbowl.scan_answers()
    HS_Techbowl.export()

    HS_Troubleshooting = questions('HS Troubleshooting', range(156,163), 163, 50)
    HS_Troubleshooting.scan_multichoice()
    HS_Troubleshooting.export()

if __name__ == '__main__':
    main()