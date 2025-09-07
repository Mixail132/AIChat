from model import model
import requests
import os
from dotenv import load_dotenv

load_dotenv()
OPENAI_API_KEY = os.environ['OPENAI_API_KEY']


def get_gpt_answer(question):
    """
    Gets the question and sends it directly to GPT
    without a middleman server. (VPN is needed)
    :param question:  the question text.
    :return: the response from GPT.
    """
    payload = {
        'model': "gpt-3.5-turbo",
        'temperature': 0.7,
        'messages': [
            {
                "role": "user",
                "content": question}]
    }
    url = 'https://api.openai.com/v1/chat/completions'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer ' + OPENAI_API_KEY
    }
    try:
        response = requests.post(url, json=payload, headers=headers)
        response_json = response.json()
        answer = response_json['choices'][0]['message']['content']
        return answer
    except Exception as ex:
        return f"There is no answer from 'gpt' model because of {ex}"


def get_gemini_answer(question):
    """
    Gets the question and sends it directly to Gemnini
    without a middleman server. (VPN is needed)
    :param question: the question text.
    :return: the response from Gemini.
    """
    response = model.generate_content(contents=[question])
    try:
        return response.text
    except Exception as ex:
        return f"{response.prompt_feedback} because of {ex}"
