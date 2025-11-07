"""
Handles email automation using SMTP.
"""
import smtplib
import yagmail
import logging
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

def send_email(config, attachments=None):
    """
    Send an email using the provided config and optional attachments.
    """
    import yagmail
    from scraper import scrape_and_save
    sender = config["sender"]
    password = config["password"]
    recipients = config["recipient"]
    subject = config.get("subject", "Automated Email")
    body = config.get("body", "This is an automated email.")

    # If scraper is enabled, get 5 job postings and use as body
    import json
    try:
        with open("config.json", "r") as f:
            full_config = json.load(f)
        scraper_config = full_config.get("scraper", {})
        if scraper_config.get("enabled"):
            job_list = scrape_and_save(scraper_config)
            body = f"Latest 5 job postings:\n\n{job_list}"
    except Exception as e:
        body = f"(Could not fetch job postings: {e})\n\n{body}"

    try:
        yag = yagmail.SMTP(user=sender, password=password)
        yag.send(to=recipients, subject=subject, contents=body, attachments=attachments)
        logging.info(f"Email sent successfully to {recipients}")
        print(f"Email sent successfully to {recipients}")
    except Exception as e:
        logging.error(f"Failed to send email: {e}")
        print(f"Failed to send email: {e}")
