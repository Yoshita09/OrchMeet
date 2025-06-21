import os
from openai import OpenAI
from dotenv import load_dotenv

# ✅ Load .env file from root project directory
load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), "..", ".env"))

client = OpenAI(
    api_key=os.getenv("AZURE_OPENAI_KEY"),
    base_url=os.getenv("AZURE_OPENAI_ENDPOINT"),
    default_headers={"api-key": os.getenv("AZURE_OPENAI_KEY")}
)

def summarize_text(text):
    response = client.chat.completions.create(
        model=os.getenv("AZURE_DEPLOYMENT_NAME"),  # This is your deployment name!
        messages=[
            {"role": "system", "content": "Summarize the meeting."},
            {"role": "user", "content": text}
        ],
        api_version=os.getenv("AZURE_API_VERSION")  # ✅ Use api_version like this, not extra_body
    )

    return response.choices[0].message.content.strip()

if __name__ == "__main__":
    print("🔍 DEPLOYMENT URL TEST")
    print(
        os.getenv("AZURE_OPENAI_ENDPOINT") + "/openai/deployments/" + os.getenv("AZURE_DEPLOYMENT_NAME") + "/"
    )

    result = summarize_text("This is a test meeting where we discussed the project goals and next steps.")
    print("\n📄 Summary:")
    print(result)
