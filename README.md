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
