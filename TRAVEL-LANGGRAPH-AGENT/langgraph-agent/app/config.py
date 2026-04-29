import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_community.utilities import SerpAPIWrapper
from duffel_api import Duffel

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
SERPAPI_API_KEY = os.getenv("SERPAPI_API_KEY")
DUFFEL_ACCESS_TOKEN = os.getenv("DUFFEL_ACCESS_TOKEN")

llm = ChatOpenAI(model="gpt-4o", temperature=0)

search_tool = SerpAPIWrapper()

client = Duffel(access_token=DUFFEL_ACCESS_TOKEN)