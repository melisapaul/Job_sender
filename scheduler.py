"""
Schedules and runs tasks based on config.json.
"""
import schedule
import time
import logging
from email_sender import send_email
from scraper import scrape_and_save
from file_organizer import organize_files
import json

def load_config():
    with open("config.json", "r") as f:
        return json.load(f)

def start_scheduler():
    config = load_config()
    email_config = config.get("email", {})
    scraper_config = config.get("scraper", {})
    file_organizer_config = config.get("file_organizer", {})

    # Schedule email task
    if email_config and email_config.get("schedule"):
        schedule.every().day.at(email_config["schedule"]).do(send_email, email_config)
        print(f"Scheduled email at {email_config['schedule']}")

    # Schedule scraper task (optional, not implemented)
    # if scraper_config.get("enabled"):
    #     schedule.every().day.at("10:00").do(scrape_and_save, scraper_config)

    # Schedule file organizer task (optional, not implemented)
    # if file_organizer_config.get("enabled"):
    #     schedule.every().day.at("11:00").do(organize_files, file_organizer_config)

    print("Scheduler started. Press Ctrl+C to exit.")
    while True:
        schedule.run_pending()
        time.sleep(1)
