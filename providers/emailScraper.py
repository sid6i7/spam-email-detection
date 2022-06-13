from imbox import Imbox
import os, sys
sys.path.insert(1, os.path.join(sys.path[0], '..'))
from config import *
import traceback

class Scraper:

    def authorize(self):

        try:
            mail = Imbox(
                hostname = "imap.gmail.com",
                username = GMAIL_ID,
                password = GMAIL_APP_PASSWORD
            )
            self.mail = mail

        except:
            print('error, could not authorize')
            print(traceback.print_exc())
        


