import os
from dotenv import load_dotenv
from openai import OpenAI

# Esto carga las variables del archivo .env al sistema
load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

try:
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "Explain what an API is."},
        ],
    )
    print(response.choices[0].message.content)
except Exception as e:
    print(f"Ups! Something's got wrong: {e}")
