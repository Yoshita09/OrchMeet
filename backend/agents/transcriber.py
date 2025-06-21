import whisper
import tempfile

model = whisper.load_model("base")

def transcribe_audio(file):
    with tempfile.NamedTemporaryFile(suffix=".mp3", delete=True) as temp:
        file.save(temp.name)
        result = model.transcribe(temp.name)
        return result['text']
