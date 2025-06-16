import os
import asyncio
from google.adk.agents import Agent
from google.adk.sessions import InMemorySessionService
from google.adk.runners import Runner
from google.genai import types
from google.genai.types import Content, Part

from dotenv import load_dotenv
import uuid


from .agent import root_agent
load_dotenv()

async def main(app_name, user_id, session_id, diff_path):

    with open(diff_path, 'r') as f:
        diff = f.read()

    session_service = InMemorySessionService()
    await session_service.create_session(app_name=app_name, user_id=user_id, session_id=session_id)

    runner = Runner(agent=root_agent, app_name=app_name,
                    session_service=session_service)

    prompt = f"Review the following PR diff:\n{diff}\n\nPlease provide a summary of the changes and any potential issues or improvements."
    user_message = Content(parts=[Part(text=prompt)], role="user")

    final_response = ""
    
    for event in runner.run(user_id=user_id, session_id=session_id, new_message=user_message):
        if event.is_final_response():
            final_response = event.content.parts[0].text
    
    print(final_response)

