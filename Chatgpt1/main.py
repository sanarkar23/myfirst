import os
from flask import Flask, jsonify
import openai

app = Flask(__name__)

# Load OpenAI API key securely from environment variable
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route('/api/funfact')
def get_fun_fact():
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": "Give me one fun, unusual, short fact. Keep it under 30 words."}
            ]
        )
        return jsonify({"fact": response['choices'][0]['message']['content']})
    except Exception as e:
        return jsonify({"error": str(e)}), 500