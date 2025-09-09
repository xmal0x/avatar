from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime
from pydantic import BaseModel
from dotenv import load_dotenv
from openai import OpenAI
from pypdf import PdfReader

load_dotenv(override=True)
openai = OpenAI()

app = FastAPI(title="Starter API")

# CORS для dev (Vite на 5173)
origins = [
  "http://localhost:5173",
  "http://127.0.0.1:5173",
]
app.add_middleware(
  CORSMiddleware,
  allow_origins=origins,
  allow_credentials=True,
  allow_methods=["*"],
  allow_headers=["*"],
)

reader = PdfReader("assets/CV_Galkin.pdf")
linkedin = ""
for page in reader.pages:
    text = page.extract_text()
    if text:
        linkedin += text

with open("assets/summary.txt", "r", encoding="utf-8") as f:
    summary = f.read()

name = "Kirill Galkin"


class Message(BaseModel):
  message: str

class History(BaseModel):
  history: list[dict]

history = []

system_prompt = f"You are acting as {name}. You are answering questions on {name}'s website, \
particularly questions related to {name}'s career, background, skills and experience. \
Your responsibility is to represent {name} for interactions on the website as faithfully as possible. \
You are given a summary of {name}'s background and LinkedIn profile which you can use to answer questions. \
Be professional and engaging, as if talking to a potential client or future employer who came across the website. \
If you don't know the answer to any question, use your record_unknown_question tool to record the question that you couldn't answer, even if it's about something trivial or unrelated to career. \
If the user is engaging in discussion, try to steer them towards getting in touch via email; ask for their email and record it using your record_user_details tool. "

system_prompt += f"\n\n## Summary:\n{summary}\n\n## LinkedIn Profile:\n{linkedin}\n\n"
system_prompt += f"With this context, please chat with the user, always staying in character as {name}."

@app.post("/api/message")
def message(payload: Message):
  messages = [{"role": "system", "content": system_prompt}] + history + [{"role": "user", "content": payload.message}]
  response = openai.chat.completions.create(
      model="gpt-4o-mini",
      messages=messages
  )

  response = response.choices[0].message.content
  history.append({'role': 'user', 'content': payload.message})
  history.append({'role': 'assistant', 'content': response})
  return {"result": response}