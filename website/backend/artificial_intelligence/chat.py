import json
import os
from dotenv import load_dotenv
import markdown

import google.generativeai as genai

load_dotenv()

genai.configure(api_key=os.getenv('GOOGLE_KEY'))

basedir = os.path.abspath(os.path.dirname(__file__))

generation_config = {
  "temperature": 0.5,
  "top_p": 1,
  "top_k": 1,
  "max_output_tokens": 2048,
}

safety_settings = [
  {
    "category": "HARM_CATEGORY_HARASSMENT",
    "threshold": "BLOCK_ONLY_HIGH"
  },
  {
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": "BLOCK_ONLY_HIGH"
  },
  {
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_ONLY_HIGH"
  },
  {
    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    "threshold": "BLOCK_ONLY_HIGH"
  },
]

model = genai.GenerativeModel(model_name="gemini-1.0-pro",
                              generation_config=generation_config,
                              safety_settings=safety_settings)

chat = model.start_chat(history=[])

instructions = """\
    DO NOT give source.
    DO NOT show any calculations.
    YOU WILL ONLY PROVIDE INFORMATION FROM THE DATA BELOW.
    THE DATA IS CORRECT.
    
    AND BEFORE ANSWERING DATA DOESNT EXIST. CHECK AGAIN!
"""


def load_ai(question):

    with open('website/backend/json_data/mayors.json') as f:
        mayor_data = json.load(f)

    with open('website/backend/json_data/user_accessories_data.json') as f:
        user_accessories_data = json.load(f)

    with open('website/backend/json_data/level_up.json') as f:
        level_up = json.load(f)

    base_prompt = f"""\
    You are a top game advisor about Hypixel Skyblock. 
    
    {instructions}
    
    Mayor Data:
    {mayor_data}
    
    User Accessories Data:
    {user_accessories_data}
    
    Best ways to level up:
    {level_up}
    
    The Question is:
    """

    response = chat.send_message(base_prompt + question).text

    return markdown.markdown(response, extensions=['md_in_html'])


def ask_ai(question):
    response = chat.send_message(instructions + question).text

    return markdown.markdown(response, extensions=['md_in_html'])

