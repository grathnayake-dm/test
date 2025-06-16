from google.adk.agents import Agent
from google.adk.tools import google_search  
from config import MODEL

code_fitcher_agent = Agent(
   name="basic_search_agent",
   model=MODEL,
   description="Agent to answer questions using Google Search.",
   instruction="You are an expert researcher. You always stick to the facts.",
   tools=[google_search]
)