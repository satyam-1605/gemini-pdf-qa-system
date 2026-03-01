import os
from dotenv import load_dotenv
import sys

from llama_index.llms.google_genai import GoogleGenAI
from IPython.display import Markdown, display
from google import genai
from google.genai import types
from exception import customexception
from logger import logging

load_dotenv()

GOOGLE_API_KEY=os.getenv("GOOGLE_API_KEY")

genai_client = genai.Client(api_key=GOOGLE_API_KEY)

def load_model():
    
    """
    Loads a Gemini-2.5-Flask model for natural language processing.

    Returns:
    - GoogleGenAI: An instance of the GoogleGenAI class initialized with the 'gemini-2.5-flask' model.
    """
    try:
        model=GoogleGenAI(model="models/gemini-2.5-flash", api_key=GOOGLE_API_KEY)
        return model
    except Exception as e:
        raise customexception(e,sys)
        