# main.py
import sys
from google import genai


def call_llm(text):

    client = genai.Client(api_key="AIzaSyCcwBMe3uxcWLN2OSsK7cQx41I93-T3AW0")

    response = client.models.generate_content(
        model="gemini-2.0-flash", contents="Explain the pull request diff:\n" + text,
    )
    print(response.text)
    print("LLM Response:", response.text)

def run(diff_path):
    with open(diff_path, 'r') as f:
        diff = f.read()
    print("🧠 Reviewing PR diff...")
    print(diff)  
    call_llm(diff)
    print("✅ Review complete.")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("❌ No diff file provided.")
    else:
        run(sys.argv[1])
