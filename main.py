from __future__ import print_function
import datetime
import os.path
from email.mime.text import MIMEText
import pyperclip
import base64

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

# Scopes for Calendar + Gmail
SCOPES = [
    "https://www.googleapis.com/auth/calendar",
    "https://www.googleapis.com/auth/gmail.send",
]


def send_email(
    creds, meet_link, recipient_name, recipient_email, event_title, start_dt
):
    """Send a professional meeting email using Gmail API."""
    try:
        gmail_service = build("gmail", "v1", credentials=creds)

        subject = f"Meeting Invitation: {event_title}"
        body = f"""Dear {recipient_name},

I hope this email finds you well.

I'd like to schedule a meeting to discuss our ongoing project and next steps. 
Please find the meeting details below:

🗓️ Title: {event_title}
📅 Date: {start_dt.strftime('%Y-%m-%d')}
⏰ Time: {start_dt.strftime('%H:%M')} UTC
🔗 Google Meet Link: {meet_link}

Please confirm your availability or suggest another suitable time if necessary.

Best regards,
Developer Advocate Demo App
"""

        message = MIMEText(body)
        message["to"] = recipient_email
        message["subject"] = subject

        raw_message = base64.urlsafe_b64encode(message.as_bytes()).decode()
        gmail_service.users().messages().send(
            userId="me", body={"raw": raw_message}
        ).execute()

        print(f"📧 Email sent successfully to {recipient_name} ({recipient_email})")

    except Exception as e:
        print(f"⚠️ Failed to send email: {e}")


def main():
    creds = None
    if os.path.exists("token.json"):
        creds = Credentials.from_authorized_user_file("token.json", SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file("credentials.json", SCOPES)
            creds = flow.run_local_server(port=0)
        with open("token.json", "w") as token:
            token.write(creds.to_json())

    service = build("calendar", "v3", credentials=creds)

    # Ask for meeting details
    print("\n📅 Schedule your meeting:")
    event_title = input("Enter meeting title: ").strip()
    date_input = input("Enter meeting date (YYYY-MM-DD): ").strip()
    start_time_input = input("Enter start time (HH:MM, 24h format): ").strip()
    duration = int(input("Enter meeting duration (minutes): ").strip())
    recipient_name = input("Enter recipient name: ").strip()
    recipient_email = input("Enter recipient email: ").strip()

    try:
        start_dt = datetime.datetime.strptime(
            f"{date_input} {start_time_input}", "%Y-%m-%d %H:%M"
        )
        end_dt = start_dt + datetime.timedelta(minutes=duration)
    except ValueError:
        print("⚠️ Invalid date or time format. Please use YYYY-MM-DD and HH:MM.")
        return

    # Create Google Calendar event with attendee
    event = {
        "summary": event_title,
        "start": {
            "dateTime": start_dt.isoformat() + "Z",
            "timeZone": "UTC",
        },
        "end": {
            "dateTime": end_dt.isoformat() + "Z",
            "timeZone": "UTC",
        },
        "attendees": [{"email": recipient_email, "displayName": recipient_name}],
        "conferenceData": {
            "createRequest": {
                "requestId": f"{event_title.lower().replace(' ', '-')}-{int(datetime.datetime.now().timestamp())}",
                "conferenceSolutionKey": {"type": "hangoutsMeet"},
            }
        },
    }

    # sendUpdates='all' sends the invite email from Google Calendar automatically
    event = (
        service.events()
        .insert(
            calendarId="primary", body=event, conferenceDataVersion=1, sendUpdates="all"
        )
        .execute()
    )

    meet_link = event.get("hangoutLink")

    print("\n✅ Meeting successfully created and invite sent!")
    print("Title:", event["summary"])
    print("Date:", start_dt.strftime("%Y-%m-%d"))
    print("Time:", start_dt.strftime("%H:%M UTC"))
    print("Meet link:", meet_link)

    # Copy meet link to clipboard
    pyperclip.copy(meet_link)
    print("📋 Meet link copied to clipboard!")

    # Send professional custom email
    send_email(creds, meet_link, recipient_name, recipient_email, event_title, start_dt)


if __name__ == "__main__":
    main()
