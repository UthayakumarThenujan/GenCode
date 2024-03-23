from configparser import ConfigParser
import google.generativeai as genai
import pptx
import streamlit as st
from pptx.util import Inches, Pt
import base64
from datetime import datetime
import os
import json
import pathlib
import textwrap
from IPython.display import display
from IPython.display import Markdown


def to_markdown(text):
    text = text.replace("•", "  *")
    indented_text = textwrap.indent(text, "\n ", predicate=lambda _: True)
    indented_text += ">"
    return indented_text


current_datetime = datetime.now()
formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M%S")

config = ConfigParser()
config.read("credentials.ini")
api_key = config["API_KEY"]["google_api_key"]

genai.configure(api_key=api_key)


TITLE_FONT_SIZE = Pt(30)
SLIDE_FONT_SIZE = Pt(16)
model_gemini_pro = genai.GenerativeModel("gemini-pro")

safety_settings = [
    {
        "category": "HARM_CATEGORY_DANGEROUS",
        "threshold": "BLOCK_NONE",
    },
    {
        "category": "HARM_CATEGORY_HARASSMENT",
        "threshold": "BLOCK_NONE",
    },
    {
        "category": "HARM_CATEGORY_HATE_SPEECH",
        "threshold": "BLOCK_NONE",
    },
    {
        "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
        "threshold": "BLOCK_NONE",
    },
    {
        "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
        "threshold": "BLOCK_NONE",
    },
]


def generate_code(topic):
    prompt = f"""i want to get the code about this topic:'{topic}."""
    response = model_gemini_pro.generate_content(
        prompt, safety_settings=safety_settings
    )
    return response
