from google.adk.agents import Agent
from .prompt import FINAL_JSON_AGGREGATOR_PROMPT

final_json_aggregator_agent = Agent(
    name='final_json_aggregator_agent',
    model="gemini-2.0-flash",
    description="Agent that merges the image data and product analysis data into a single, structured JSON output.",
    instruction= FINAL_JSON_AGGREGATOR_PROMPT
)
