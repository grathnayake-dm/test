from google.adk.agents import Agent
from google.adk.tools import google_search  
from config import MODEL

static_analysis_agent = Agent(
   name="static_analysis_agent",
   model=MODEL,
   description="Detect formatting and basic errors",
   instruction=" Flags code style issues, unused variables, missing docstrings",
   tools=[google_search]
)