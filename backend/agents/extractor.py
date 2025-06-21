import openai

def extract_tasks(transcript):
    # Dummy task extractor — improve with NLP later
    lines = transcript.split('\n')
    tasks = []
    for line in lines:
        if any(kw in line.lower() for kw in ['todo', 'task', 'assign', 'follow up']):
            tasks.append(line.strip())
    return "\n".join(tasks)
