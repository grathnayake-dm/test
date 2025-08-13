from google.adk.agents import SequentialAgent, ParallelAgent

from .sub_agents.searching.agent import product_analysis_agent
from .sub_agents.get_url.agent import product_page_calling_agent
from .sub_agents.json_gen.agent import final_json_aggregator_agent
from .sub_agents.screens.agent import screen_capturing_agent

parallel_pipeline_agent = ParallelAgent(
    name= "paralle_webscraping_pipline",
    sub_agents=[screen_capturing_agent, product_analysis_agent],
    description="Execute the parallel workflow.",
)

sequential_pipeline_agent = SequentialAgent(
     name="structured_product_pipeline",
     sub_agents=[product_page_calling_agent, parallel_pipeline_agent, final_json_aggregator_agent],
     description="Coordinates agents and synthesizes the results. return output as a json file"
 )

root_agent = sequential_pipeline_agent
