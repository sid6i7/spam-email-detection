import streamlit as st
import sys
sys.path.append('app')
from config import *
from providers.emailScraper import *


class Interface:

    def __init__(self) -> None:
        st.title("Email Clasdsifier")
        st.text("Scanning {}".format(GMAIL_ID))

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

        self.emails = parsedEmails
    
    def display_email(self, idx):
        subject = self.emails[idx]['subject']
        body = self.emails[idx]['body']

        st.text('Subject: {}'.format(subject))
        st.text(body)

i = Interface()
emails = []

col1, col2, col3, col4, col5, col6 = st.columns(6)

previousEmail = col1.button("Previous")
scan = col2.button("Scan")
scanned = False
nextEmail = col3.button("Next")
idx = 0

if(scan):
    i.scan_emails()
    scanned = True
    idx = 0
    i.display_email(idx)

if(nextEmail):
    if emails:
        if len(emails) - 1 >= idx:
            idx += 1
            i.display_email(idx)
        else:
            st.error("no next email")
    if scanned:
        st.info("No new emails")
    else:
        st.error("Scan the email first")

if(previousEmail):
    if idx > 0:
        idx -= 1
        i.display_email(idx)
    else:
        st.error("no previous email")

    



    
    
            


    # st.text("scanning for new emails")
    # emails = scraper.get_unread_emails()
    # for email in emails: