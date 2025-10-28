# 🚀 Google Calendar Meeting Automation

A smart and streamlined Python tool that automates your entire meeting workflow — from scheduling to notifications — with seamless Google integration.

## ✨ Features

- **📅 Interactive Meeting Scheduling** — Easily input meeting title, date, time, and duration  
- **👥 Automatic Attendee Management** — Instantly adds participants to your Google Calendar event  
- **🔗 Google Meet Integration** — Auto-generates a unique Meet link for every event  
- **✉️ Email Invitations** — Sends polished, professional meeting invites via the Gmail API  
- **📋 Clipboard Support** — Instantly copies the Meet link for quick sharing  
- **🧠 Secure OAuth 2.0 Authentication** — Enables safe and persistent access to Google APIs  

## 🧰 Tech Stack

- **Language:** Python 3.10+  
- **APIs:** Google Calendar API, Google Gmail API  
- **Libraries:**  
  - `google-auth`, `google-auth-oauthlib`, `google-auth-httplib2`  
  - `google-api-python-client`  
  - `pyperclip` (for clipboard functionality)


## ⚙️ How It Works

1. **Authenticate** — Sign in with your Google account via the OAuth 2.0 flow.  
2. **Input Details** — Provide meeting title, date, time, duration, and attendee details.  
3. **Automation in Action:**  
   - Creates a Google Calendar event with a Meet link  
   - Adds the attendee to the event automatically  
   - Sends a personalized invitation email via Gmail  
   - Copies the Meet link to your clipboard for instant sharing  
## 🧑‍💻 Setup

1. **Clone the repository**  
   ```bash
   git clone https://github.com/yourusername/meeting-automation.git
   cd meeting-automation
   ```

2. **Install dependencies**
    ```bash
    pip install -r requirements.txt
    ```

3. **Configure OAuth credentials**

- Create credentials on the Google Cloud Console
- Enable Google Calendar API and Gmail API.
- Download your credentials.json and place it in the project root.

4. **Run the script**
    ```bash
    python main.py
    ```


Developer Diary — Google Meet Scheduler
 Overview
This project demonstrates an integration between Google Calendar, Google Meet, and Gmail APIs to automate the scheduling and invitation process for meetings.
It allows the user to:
•	Schedule a meeting by entering its title, date, time, duration, and recipient details
•	Automatically generate a Google Meet link
•	Add the recipient as an attendee (meeting appears in their calendar)
•	Send a personalized professional email with meeting details
•	Copy the Meet link directly to the clipboard for convenience
________________________________________
 How I Approached the Task
1. Setup and Exploration
•	Started by setting up a new Python environment and installing the required dependencies:
	 pip install google-api-python-client google-auth google-auth-oauthlib google-auth-httplib2 pyperclip
•	Created a Google Cloud project and enabled the following APIs:
o	Google Calendar API
o	Gmail API
•	Downloaded the credentials.json file and placed it in the working directory for OAuth authentication.
2. Initial Implementation
•	Followed Google’s quickstart examples for the Calendar API to create and list events.
•	Extended the logic to insert a new event with conferenceData to auto-generate a Google Meet link.
•	Added Gmail API integration to send meeting details via email.
•	Implemented clipboard support using pyperclip to copy the Meet link instantly.
3. Key Design Decisions
•	Used OAuth 2.0 with token persistence (token.json) to simplify repeated runs.
•	Added interactive input prompts (title, date, time, duration, recipient) to make the script user-friendly and demo-ready.
•	Included the recipient as an event attendee and used sendUpdates='all' to automatically send Google Calendar invitations.
•	Chose to keep the user email template clean and professional, suitable for real-world use by a developer advocate.
________________________________________
 Issues and How I Solved Them
Issue	Description	Solution
Authentication Scope Error	Gmail API returned 403: Insufficient Permission when sending emails.	
Deleted token.json and re-authenticated after adding https://www.googleapis.com/auth/gmail.send to SCOPES.
Package Import Error (pyparsing):	
Older Python version caused an AttributeError in pyparsing.	Installed Python 3.11 and re-installed dependencies in a clean environment.
Event not visible to recipient:	
The event appeared only in the organizer’s calendar.	
Added the recipient as an attendee and set sendUpdates='all' in the events.insert() call.
Clipboard support not working	Windows environment needed an external library.	Installed and used the pyperclip package for reliable cross-platform clipboard access.
________________________________________
 Resources and Documentation Used
•	Google API Python Client Documentation:
https://developers.google.com/api-client-library/python/
•	Google Calendar API Guides:
https://developers.google.com/calendar/api/guides/create-events
•	Gmail API Documentation:
https://developers.google.com/gmail/api
•	OAuth 2.0 Setup and Consent Screen Configuration:
https://developers.google.com/identity/protocols/oauth2
•	Pyperclip library documentation for clipboard handling.
________________________________________
Reflection
This task provided a great opportunity to explore how different Google APIs can work together to build a complete, real-world workflow.
I focused on developer experience by making the script simple, interactive, and extensible — aligning with the mindset of a Developer Advocate who bridges engineering with communication and usability.

