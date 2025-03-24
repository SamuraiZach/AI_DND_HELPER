import os
from flask import Flask, render_template, request
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)

token = os.getenv["GITHUB_TOKEN"]
endpoint = "https://models.inference.ai.azure.com";
modelName = "gpt-4o";
client = OpenAI(
    base_url=endpoint,
    api_key=token,
)

@app.route('/')
def hello_world():
    return 'Hello from Flask!'

