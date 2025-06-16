from google.adk.agents import Agent, SequentialAgent, ParallelAgent
from google.adk.tools import google_search  
from config import MODEL
from .subagents.code_fetcher_agent.agent import code_fitcher_agent
from .subagents.code_review_agent.agent import code_review_agent
from .subagents.static_analysis_agent.agent import static_analysis_agent


# parallel_pipeline = ParallelAgent(
#     name="parallel_pipeline_agent",
#     sub_agents=[],
#     description=""
# )
sequential_pipeline = SequentialAgent(
    name = "sequential_pipeline_agent",
    sub_agents=[code_fitcher_agent, static_analysis_agent, code_review_agent],
    description="call the cade fitcher agent"
)

root_agent = sequential_pipeline