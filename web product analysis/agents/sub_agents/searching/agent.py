from google.adk.agents import Agent
from google.adk.tools import google_search
from model import MODEL
from .prompt import PRODUCT_ANALYSIS_PROMPT

product_analysis_agent = Agent(
    name="product_analysis_agent",
    model=MODEL,
    description=(
        "You are a product analysis agent."
    ),
    instruction=PRODUCT_ANALYSIS_PROMPT,
    tools=[google_search],
    output_key="search_results",
)
