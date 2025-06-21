from google.oauth2 import service_account
from googleapiclient.discovery import build
import datetime
import os

def schedule_tasks(task_text):
    # You’ll replace this with parsed task dicts
    creds = service_account.Credentials.from_service_account_file(
        'credentials.json',
        scopes=['https://www.googleapis.com/auth/calendar']
    )
    service = build('calendar', 'v3', credentials=creds)

    # Dummy task parsing — refine later
    for line in task_text.split('\n'):
        if not line.strip(): continue
        event = {
            'summary': line.strip(),
            'start': {'dateTime': '2025-06-22T10:00:00+05:30', 'timeZone': 'Asia/Kolkata'},
            'end': {'dateTime': '2025-06-22T11:00:00+05:30', 'timeZone': 'Asia/Kolkata'},
        }
        service.events().insert(calendarId='primary', body=event).execute()
