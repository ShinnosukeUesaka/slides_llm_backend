from pathlib import Path
from fastapi import FastAPI, Header
from urllib.parse import urlencode

from pydantic import BaseModel
from openai import Client, OpenAI
from typing import Annotated
from starlette.middleware.cors import CORSMiddleware
from tempfile import TemporaryDirectory
import dotenv
import os
import datetime
from slides_llm.firebase_utils import db
import uuid


client = OpenAI()


# storage = storage.bucket("speaking-53cb7.appspot.com")

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
from fastapi import FastAPI, HTTPException, Body
from pydantic import BaseModel, Field
from typing import List, Optional

app = FastAPI()

# test endpoint
@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/conversation")
def create_conversation():
    # create id
    conversation_id = str(uuid.uuid4())
    # create conversation
    conversation = {
        "id": conversation_id,
        "created_at": datetime.datetime.now(),
        "messages": [],
    }
    # save conversation
    db.collection("conversations").document(conversation_id).set(conversation)
    return conversation

@app.post("/conversation/{conversation_id}/message")
def create_message(conversation_id: str, message: str):
    # get conversation
    conversation_ref = db.collection("conversations").document(conversation_id)
    conversation = conversation_ref.get().to_dict()
    # create message
    message = {
        "id": str(uuid.uuid4()),
        "created_at": datetime.datetime.now(),
        "message": message,
    }
    # save message
    conversation["messages"].append(message)
    conversation_ref.set(conversation)
    return conversation
