from google.adk.agents import Agent
from google.adk.tools import google_search  
from config import MODEL

code_review_agent = Agent(
   name="code_review_agent",
   model=MODEL,
   description="Review logic, readability, naming conventions, and more complex patterns.",
   instruction="Provides natural language explanations, suggestions, and improvements.",
   tools=[google_search]
)