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

# 3e567ec8


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
