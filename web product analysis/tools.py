# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# from typing import List
# from google.adk.agents import Agent


# def extract_links_from_url(url: str) -> List[str]:
#     options = Options()
#     options.add_argument("--headless=new")
#     options.add_argument("--no-sandbox")
#     options.add_argument("--disable-dev-shm-usage")

#     driver = webdriver.Chrome(options=options)
#     try:
#         driver.get(url)
#         links = [a.get_attribute('href') for a in driver.find_elements("tag name", "a")]
#         return [link for link in links if link]
#     finally:
#         driver.quit()


# blog_page_calling_agent = Agent(
#     name="blog_page_calling_agent",
#     model="gemini-2.0-flash",
#     description="Identifies and extracts content topics from blog or newsletter pages within the given website.",
#     tools=[extract_links_from_url],
#     instruction="""
# You are given a company's main website URL.

# 1. Use the `extract_links_from_url` to get all the sub-URLs from that website.
# 2. Search for sub-URLs that look like they may lead to blogs or newsletters (e.g., containing `/blog`, `/insights`, `/news`, `/articles`).
# 3. Visit the most relevant one.
# 4. Analyze the content of that page. Your goal is to:
#    - Identify the topics or themes discussed in the blog or newsletter.
#    - Focus on summaries or headlines if available.

# output : 
# eturn a JSON with:
# {
#   "blog_page_url": "<final blog/newsletter page>",
# }
# """
# )
















# main.py
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import uuid
import asyncio
from dotenv import load_dotenv
from google.adk import Runner
from google.adk.sessions import InMemorySessionService
from google.genai.types import Content, Part
from agents.agent import root_agent

load_dotenv()

app = FastAPI()

class AgentRequest(BaseModel):
    url: str  

@app.post("/run-agent")
async def run_agent_on_paper(request: AgentRequest):
    app_name = "research_app"
    user_id = "user_" + str(uuid.uuid4())[:8]       
    session_id = "session_" + str(uuid.uuid4())[:8]  

    session_service = InMemorySessionService()
    await session_service.create_session(app_name=app_name, user_id=user_id, session_id=session_id)

    runner = Runner(agent=root_agent, app_name=app_name, session_service=session_service)
    
    prompt = f"Analyze the products provided by the organization at  <url>{request.url}</url>. Identify relevant product pages, extract key information, and return a comprehensive JSON summary."
    user_message = Content(parts=[Part(text=prompt)], role="user")

    final_response = ""
    try:
        for event in runner.run(user_id=user_id, session_id=session_id, new_message=user_message):
            if event.is_final_response():
                final_response = event.content.parts[0].text
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

    return {"response": final_response}


