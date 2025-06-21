from flask import Flask, request, jsonify
from agents.transcriber import transcribe_audio
from agents.summarizer import summarize_text
from agents.extractor import extract_tasks
from agents.scheduler import schedule_tasks
from agents.notifier import send_notification
from flask_cors import CORS
from dotenv import load_dotenv
import os

load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), ".env"))


app = Flask(__name__)
CORS(app)

@app.route('/upload', methods=['POST'])
def handle_upload():
    file = request.files['audio']
    transcript = transcribe_audio(file)
    summary = summarize_text(transcript)
    tasks = extract_tasks(transcript)
    schedule_tasks(tasks)
    send_notification(summary, tasks)
    return jsonify({"transcript": transcript, "summary": summary, "tasks": tasks})

if __name__ == '__main__':
    app.run(debug=True)
