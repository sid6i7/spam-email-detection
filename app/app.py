import streamlit as st
from config import *
from providers.emailScraper import *
from utils.emailClassifier import *
import json
class Interface:

    def __init__(self) -> None:
        st.title("Email Clasdsifier")
        st.info("Email: {}".format(GMAIL_ID))

        self.scraper = Scraper()
        self.scraper.authorize()
    
    def scan_emails(self):
        emails = self.scraper.get_unread_emails()
        parsedEmails = []
        for email in emails:
            parsedEmails.append({
                'subject': email[0],
                'body': email[1]
            })
        with open(os.path.join(EMAIL_DIR, 'emails.json'), 'w+') as f:
            json.dump(parsedEmails, f)
    
    def display_emails(self, emails):
        for idx, email in enumerate(emails):
            st.text("Email no. {}".format(idx + 1))
            subject = email['subject']
            body = email['body']

            st.text('Subject: {}'.format(subject))
            st.text(body)
            typeOfEmail = Classifier().predict_email(subject + body)
            st.success("Email is {}".format(typeOfEmail))
            st.text('=======================================================')

if __name__ == "__main__":

    i = Interface()
    emails = []

    with st.sidebar:
        st.header('Options')
        choice = st.radio(
            "",
            ("Scan", "Display")
        )
        scanned = False

    if choice == 'Scan':
        scan = st.button("Scan")
        if(scan):
            i.scan_emails()
            st.text('scanning complete')
            scanned = True
    
    if choice == 'Display':
        emailsPath = os.path.join(EMAIL_DIR, 'emails.json')
        if os.path.isfile(emailsPath):
            with open(emailsPath, 'r') as f:
                emails = json.load(f)
                if emails:
                    i.display_emails(emails)
                    os.remove(emailsPath)
                else:
                    st.error("no emails found")      
        else:
            st.text("scan first")
                

        

    



    
    
            


    # st.text("scanning for new emails")
    # emails = scraper.get_unread_emails()
    # for email in emails: