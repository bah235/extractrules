import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s:%(name)s:%(levelname)s:%(message)s')
file_handler = logging.FileHandler('app.log')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

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
        logger.error(text)
    
    elif status == 'WARN':
        print(f"{bcolors.WARNING}{text}{bcolors.ENDC}")
        logger.warning(text)
      
    elif status == 'OK':
        print(f"{bcolors.OKGREEN}{text}{bcolors.ENDC}")
        logger.info(text)
      
    else:
        logger.info(text)
