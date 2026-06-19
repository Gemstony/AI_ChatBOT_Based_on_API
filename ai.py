from fastapi import FastAPI
from pydantic import BaseModel
import os
from groq import Groq
from dotenv import load_dotenv
from fastapi.middleware.cors import CORSMiddleware

load_dotenv(dotenv_path=".env")


api_key = os.getenv("API_KEY")

if not api_key:
    raise Exception("API KEY not found in env file")

# creating a client using Grok
client = Groq(api_key = api_key)

# starting FastAPI
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://scartech.kesug.com"],
    allow_methods=['POST'],
    allow_headers=["*"]
)

class ChatRequest(BaseModel):
    user_message: str

class ChatResponse(BaseModel):
    bot_reply: str

# this history will be reseting every time server restart
conversation_history = []

# system prompt fro specialization

SYSTEM_PROMPT = """You are a friendly customer support assistant for a pizza shop.
Your name is 'PizzaBot'. Keep responses under 2 sentences. Be cheerful."""

# function that call the AI

def get_ai_reply(user_message: str) -> str:
    # creating list of messages

    try:
        messages = [
            {
                "role": "system",
                "content": SYSTEM_PROMPT,
            },
            *conversation_history,

            {
                "role": "user",
                "content": user_message
            }

        ]

        # send request to AI

        response = client.chat.completions.create(
            model = "llama-3.3-70b-versatile",
            messages = messages,
            temperature = 0.7 # this controller the creativity of the model 0 = strictly 1 = creative
        )

        # response from API

        ai_reply = response.choices[0].message.content

        # updating the conversation history so the AI remembers

        conversation_history.append({"role": "user", "content": user_message})
        conversation_history.append({"role": "assistant", "content": ai_reply})

        return ai_reply
    
    except Exception as e:
        print(f"Error occurred: {e}")
        return "I'm sorry, but I encountered an error while processing your request."

# the post endpoint that will be calling the get ai reply function

@app.post("/chat", response_model = ChatResponse)
async def chat_endpoint(request: ChatRequest):
    user_text = request.user_message

    ai_text = get_ai_reply(user_text)

    return ChatResponse(bot_reply = ai_text)

