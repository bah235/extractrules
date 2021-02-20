class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def pdf_log(text, status=None):
    if status == 'FAIL':
        print(f"{bcolors.FAIL}{text}{bcolors.ENDC}")
    
    elif status == 'WARN':
        print(f"{bcolors.WARNING}{text}{bcolors.ENDC}")
      
    elif status == 'OK':
        print(f"{bcolors.OKGREEN}{text}{bcolors.ENDC}")
      
    else:
        print(text)
