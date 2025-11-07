# Dry-run test for email_sender.send_email
# This script monkeypatches yagmail.SMTP to avoid real network calls.
import yagmail
from email_sender import send_email

class FakeSMTP:
    def __init__(self, user=None, password=None, *args, **kwargs):
        self.user = user
        self.password = password
    def send(self, to, subject, contents, attachments=None):
        print("DRYRUN: send called")
        print("  user:", self.user)
        print("  to:", to)
        print("  subject:", subject)
        # contents could be string or list; print short preview
        if isinstance(contents, str):
            print("  contents_preview:", contents[:300].replace('\n','\\n'))
        else:
            print("  contents_preview:", str(contents)[:300])
        print("  attachments:", attachments)

# Patch yagmail.SMTP to our fake
yagmail.SMTP = FakeSMTP

# Minimal test config
config = {
    "sender": "test-sender@example.com",
    "password": "fake-password",
    "recipient": ["recipient@example.com"],
    "subject": "Test dry-run",
    "body": "This is a dry-run test of email_sender.send_email"
}

if __name__ == '__main__':
    send_email(config, attachments=None)
