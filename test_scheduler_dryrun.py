# Test scheduler functionality without infinite loop or real email sending
import schedule
import json
import yagmail
from scheduler import load_config
from email_sender import send_email

# Mock yagmail to prevent real email sending
class FakeSMTP:
    def __init__(self, user=None, password=None, *args, **kwargs):
        self.user = user
        print(f"DRYRUN: Created SMTP connection for {user}")
    
    def send(self, to, subject, contents, attachments=None):
        print(f"DRYRUN: Would send email")
        print(f"  To: {to}")
        print(f"  Subject: {subject}")
        print(f"  Content preview: {str(contents)[:100]}...")
        return True

# Patch yagmail
yagmail.SMTP = FakeSMTP

def test_scheduler_setup():
    """Test if scheduler can load config and set up jobs without running them"""
    print("=== Testing Scheduler Setup ===")
    
    try:
        # Test config loading
        config = load_config()
        print("✓ Config loaded successfully")
        print(f"  Email schedule: {config.get('email', {}).get('schedule')}")
        print(f"  Scraper enabled: {config.get('scraper', {}).get('enabled')}")
        
        # Test scheduling setup (without starting the loop)
        email_config = config.get("email", {})
        if email_config and email_config.get("schedule"):
            schedule.every().day.at(email_config["schedule"]).do(send_email, email_config)
            print(f"✓ Email scheduled for {email_config['schedule']}")
            
            # Show scheduled jobs
            jobs = schedule.get_jobs()
            print(f"✓ Total scheduled jobs: {len(jobs)}")
            for i, job in enumerate(jobs):
                print(f"  Job {i+1}: {job}")
        
        # Test if we can manually trigger the email function (dry run)
        print("\n=== Testing Manual Email Trigger ===")
        send_email(email_config)
        
        print("\n✓ Scheduler test completed successfully!")
        return True
        
    except Exception as e:
        print(f"✗ Scheduler test failed: {e}")
        return False

if __name__ == "__main__":
    success = test_scheduler_setup()
    
    # Clear scheduled jobs to clean up
    schedule.clear()
    
    if success:
        print("\n🎉 The scheduler code is working! It can:")
        print("  - Load config.json")
        print("  - Schedule email tasks") 
        print("  - Execute email sending (dry run)")
        print("\nTo run the actual scheduler: python main.py")
        print("(Warning: This will send real emails based on your config)")
    else:
        print("\n❌ The scheduler has issues that need to be fixed")