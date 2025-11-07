# Product Requirements Document (PRD)
**Project Name:** Python Task Automation & Scheduler

## 1. Objective
Build a lightweight Python-based automation tool that can perform scheduled tasks like:
- Sending automated emails
- Web scraping and saving results
- Organizing files into folders

The tool should be easy to run, require no database, and log all task executions.

---

## 2. Features

### 2.1 Email Automation
- Use SMTP (Gmail, Outlook, etc.) to send emails.
- Allow plain text and HTML content.
- Support attachments (CSV, PDF).
- Configurable sender, recipient(s), subject, and message.
- Example use case: Send a daily status report at 9:00 AM.

### 2.2 Task Scheduling
- Use `schedule` or `APScheduler`.
- Support recurring tasks: hourly, daily, weekly.
- Run multiple tasks concurrently.
- Example: Scrape job listings every 24 hours and send results via email.

### 2.3 Web Scraping (Optional)
- Fetch data from a website (jobs, news, weather, etc.).
- Parse HTML with `BeautifulSoup`.
- Save results in CSV/Excel.
- Example: Scrape the latest 10 job postings and export them.

### 2.4 File Organizer (Optional)
- Scan a given directory.
- Move files into subfolders based on extension (PDF → `/Documents`, JPG → `/Images`).
- Example: Clean up `Downloads` folder automatically.

---

## 3. Non-Functional Requirements
- **Cross-platform**: Should run on Windows, Linux, or Mac.
- **No Database**: Use flat files (CSV/JSON/logs).
- **Configuration**: Store user settings in a `config.json` file (e.g., email credentials, task schedule).
- **Logging**:
  - Maintain `log.txt` for task execution history.
  - Record success/failure of each task.
- **Lightweight**: Should run with minimal dependencies.

---

## 4. Inputs & Outputs

### Inputs:
- `config.json`: Contains user settings (email credentials, scraping URL, folder paths).

### Outputs:
- `log.txt`: Task execution log.
- `results.csv` / `results.xlsx`: Scraped data export (if scraping enabled).
- Organized file directories (if file organizer enabled).

---

## 5. Example Workflow

1. User configures `config.json` like this:
```json
{
  "email": {
    "sender": "your_email@gmail.com",
    "password": "app_password",
    "recipient": ["user1@gmail.com", "user2@gmail.com"],
    "subject": "Daily Report",
    "schedule": "09:00"
  },
  "scraper": {
    "enabled": true,
    "url": "https://example.com/jobs",
    "schedule": "daily"
  },
  "file_organizer": {
    "enabled": true,
    "path": "C:/Users/Downloads"
  }
}
```

Scheduler starts.

At 9:00 AM → Email is sent.

At configured interval → Website scraped → results saved in results.csv.

File organizer runs → moves files into folders.

Logs are written into log.txt.

6. Folder Structure
automation-tool/
│── main.py            # Entry point
│── email_sender.py    # Email automation logic
│── scraper.py         # Web scraping logic
│── file_organizer.py  # File automation logic
│── scheduler.py       # Scheduling tasks
│── config.json        # User settings
│── log.txt            # Execution logs
│── requirements.txt   # Dependencies
│── README.md          # Documentation
│── PRD.md             # Product Requirements Document
