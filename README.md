# OrchMeet - Autonomous Meeting Assistant

OrchMeet is a smart multi-agent system that processes meeting audio files and provides automated **transcription**, **summarization**, **task extraction**, **calendar scheduling**, and **notifications**. Designed for professionals and teams to save time and maximize productivity.

[OrchMeet Demo](https://drive.google.com/file/d/1rtj_Y65frHkgEmNARnwirh0eBF88A7pf/view?usp=drive_link)

[OrchMeet Live](https://yoshita09.github.io/OrchMeet/) <!-- Optional -->

---

## 🚀 Features

- 🎧 Upload meeting audio (`.mp3`)
- ✍️ Real-time transcription using [Whisper](https://github.com/openai/whisper)
- 🧠 Intelligent summarization using GPT-4o via Azure OpenAI
- 📋 Task extraction using NLP prompts
- 📅 Automatic Google Calendar scheduling 
- 🔔 Email/SMS notifications with meeting summary and tasks

---

## 🛠️ Tech Stack

| Layer        | Technology                        |
|-------------|------------------------------------|
| Frontend     | HTML, CSS, JavaScript             |
| Backend      | Python, Flask, OpenAI SDK         |
| Agents       | Whisper, GPT-4o (Azure), Custom NLP |
| Hosting/Test | Localhost (Flask & HTTP Server)   |
| API          | Azure OpenAI API (`2024-12-01-preview`) |

---

## 📁 Folder Structure

```
OrchMeet/
├── backend/
│ ├── app.py
│ ├── .env
│ └── agents/
│ ├── transcriber.py
│ ├── summarizer.py
│ ├── extractor.py
│ ├── scheduler.py
│ └── notifier.py
├── frontend/
│ └── index.html
├── venv/
└── requirements.txt
```
---
### 🤖 Agents Overview

| Agent Name     | File             | Description                                                                 | Input             | Output                      | Dependencies                                 |
|----------------|------------------|-----------------------------------------------------------------------------|-------------------|-----------------------------|----------------------------------------------|
| **Transcriber**| `transcriber.py` | Converts uploaded `.mp3` meeting audio into raw transcript text using Whisper | Audio file (.mp3) | Transcript text             | `openai-whisper`                             |
| **Summarizer** | `summarizer.py`  | Uses Azure OpenAI (GPT-4o) to generate a meeting summary from transcript    | Transcript text   | Summary text                | `openai`, `.env`           |
| **Extractor**  | `extractor.py`   | Extracts actionable tasks and to-dos from the transcript                     | Transcript text   | List of tasks               | `openai`                                     |
| **Scheduler**  | `scheduler.py`   | Adds extracted tasks to Google Calendar                                     | Task list         | Google Calendar events      | `google-api-python-client`, `oauth2client`   |
| **Notifier**   | `notifier.py`    | Sends meeting summary and tasks via email or Slack webhook                  | Summary + tasks   | Notification sent           | `smtplib`, `email`, `requests`               |


---
### 📌 Example Workflow
Upload .mp3 meeting audio

Whisper transcribes audio

GPT-4o summarizes transcript

Tasks are extracted and displayed

Schedule and notify features can be triggered

---

## ⚙️ Setup Instructions

### 1. Clone the Repo

```
git clone https://github.com/your-username/OrchMeet.git
cd OrchMeet
```
### 2. Create and Activate Virtual Environment
```
python3 -m venv venv
source venv/bin/activate  # Mac/Linux
```
### 3. Install Dependencies
```
pip install -r requirements.txt
```
### 4. Configure .env File
Create a .env file in the /backend/ directory with your Azure OpenAI credentials:
```AZURE_OPENAI_KEY=your_azure_api_key
AZURE_OPENAI_ENDPOINT=https://your-resource-name.openai.azure.com
AZURE_DEPLOYMENT_NAME=your-deployment-name
AZURE_API_VERSION=2024-12-01-preview
```
### 5. Start Backend Server
```
cd backend
python3 app.py
```
### 6. Start Frontend
```
cd frontend
python3 -m http.server 3002
```

---

## 👩‍💻 Made by

**Yoshita Singhal**

- GitHub: [@yoshita09](https://github.com/yoshita09)
- LinkedIn: [Yoshita Singhal](https://linkedin.com/in/yoshita09)


---




