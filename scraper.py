"""
Handles web scraping tasks.
"""

import logging
import requests
from bs4 import BeautifulSoup

def scrape_and_save(config):
    """
    Scrape data from a website (Naukri.com) using Selenium and return the latest 5 job postings as a string.
    """
    url = config.get("url")
    if not url:
        return "No URL provided."
    try:
        response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"}, timeout=10)
        soup = BeautifulSoup(response.text, "html.parser")
        jobs = []
        # remoteok.com: job postings are in <tr class="job">
        job_cards = soup.find_all("tr", class_="job")
        print(f"[DEBUG] Found {len(job_cards)} job cards on the page.")
        for card in job_cards[:5]:
            try:
                title = card.find("h2").get_text(strip=True)
            except Exception:
                title = "(No title)"
            try:
                company = card.find("h3").get_text(strip=True)
            except Exception:
                company = "(No company)"
            try:
                location = card.find("div", class_="location").get_text(strip=True)
            except Exception:
                location = "(No location)"
            jobs.append(f"{title} | {company} | {location}")
        if not jobs:
            print("[DEBUG] No jobs found after extraction.")
            return "No jobs found."
        return "\n".join(jobs)
    except Exception as e:
        return f"Scraping failed: {e}"
    except Exception as e:
        return f"Scraping failed: {e}"
