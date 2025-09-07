import os
import requests
from dotenv import load_dotenv

load_dotenv()
GEMINI_API_KEY = os.environ['GEMINI_API_KEY']


def get_gemini_answer(prompt):
    """
    Gets the question and sends it directly to Gemini
    without a middleman server. (VPN is needed ?)
    :param prompt:  the question text.
    :return: the response from GPT.
    """
    url = (
        f"https://generativelanguage.googleapis.com/"
        f"v1beta/models/gemini-2.0-flash:generateContent"
    )
    headers = {
        "Content-Type": "application/json",
        "X-goog-api-key": GEMINI_API_KEY
    }

    payload = {"contents": [
        {"parts": [{"text": f"{prompt}"}]}
    ]}

    try:
        response = requests.post(url, json=payload, headers=headers)
        response_json = response.json()
        answer = response_json["candidates"][0]["content"]["parts"][0]["text"]
        return answer
    except Exception as ex:
        return f"There is no answer from 'gemini' model because of {ex}"
