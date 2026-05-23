import os
import json
from dotenv import load_dotenv
import google.generativeai as genai

from app.prompts import SYSTEM_PROMPT

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-1.5-flash")

def generate_workflow(user_prompt):

    final_prompt = f"""
    {SYSTEM_PROMPT}

    User Request:
    {user_prompt}
    """

    try:

        response = model.generate_content(final_prompt)

        text = response.text.strip()

        text = text.replace("```json", "")
        text = text.replace("```", "")

        workflow_json = json.loads(text)

        return workflow_json

    except Exception as e:

        return {
            "error": str(e)
        }