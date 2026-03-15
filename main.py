# -*- coding: utf-8 -*-
"""
Created on Sun Mar 15 13:30:30 2026

@author: praveyad
"""

import os
from fastapi import FastAPI
from pydantic import BaseModel
import google.generativeai as genai

app = FastAPI()

# 1. Setup Gemini (API Key will come from Cloud Settings, not hardcoded)
genai.configure(api_key=os.environ.get("GEMINI_API_KEY"))
model = genai.GenerativeModel(
    model_name="gemini-2.5-flash",
    system_instruction="You are a Socratic AI Tutor for the NCERT syllabus..."
)

# 2. Define what the incoming data looks like
class ChatRequest(BaseModel):
    message: str

# 3. Create the API Endpoint
@app.post("/chat")
async def chat_endpoint(request: ChatRequest):
    # In a simple version, we start a new chat each time. 
    # For a real app, you'd pass history here too.
    chat = model.start_chat(history=[])
    response = chat.send_message(request.message)
    return {"reply": response.text}

@app.get("/")
def health_check():
    return {"status": "AI Tutor is online"}

