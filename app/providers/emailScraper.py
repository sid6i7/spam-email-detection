from imbox import Imbox
import os, sys
sys.path.insert(1, os.path.join(sys.path[0], '..'))
from config import *
import traceback

class Scraper:

    def authorize(self):
        """Authenticates with the gmail API"""
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
    

    def get_unread_emails(self):
        """Fetches all the unread emails and returns subject + body"""
        emails = []
        messages = self.mail.messages(unread = True)
        
        for (uid, message) in messages:
            self.mail.mark_seen(uid)
            email = []
            email.append(message.subject)
            email.append(message.body['plain'][0])
            emails.append(email)

        return emails
        


