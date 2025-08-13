# Within a session, a state acts like the scratch pad for the interaction
# Session.events hold the history of the interaction
# Session.state provides a temporary store to the agent where dynamic details are updated
from dotenv import load_dotenv
from google.adk import Runner
from google.adk.agents import LlmAgent
from google.adk.sessions import InMemorySessionService
from google.genai.types import Content, Part

load_dotenv()

model="gemini-2.0-flash"

# Define agent with output_key
root_agent = LlmAgent(
    name="Math",
    model=model,
    instruction="You are an excellent math teacher",
    output_key="final_result" # Save response to state['final_result']
)

# --- Setup Runner and Session ---
app_name, user_id, session_id = "state_app", "user1", "session1"
session_service = InMemorySessionService()
runner = Runner(
    agent=root_agent,
    app_name=app_name,
    session_service=session_service
)
session = session_service.create_session(app_name=app_name,
                                        user_id=user_id,
                                        session_id=session_id)
print(f"Initial state: {session.state}")

# --- Run the Agent ---
# Runner handles calling append_event, which uses the output_key
# to automatically create the state_delta.
user_message = Content(parts=[Part(text="what will be sum of 5 and 6?")],role="user")
for event in runner.run(user_id=user_id,
                        session_id=session_id,
                        new_message=user_message):
    print(f"event is: ", event)
    if event.is_final_response():
      print(f"Agent responded.") # Response text is also in event.content

# --- Check Updated State ---
updated_session = session_service.get_session(app_name=app_name, user_id=user_id, session_id=session_id)

print(f"Sessions (`updated_session`): , {updated_session}")

print(f"session id : {updated_session.id}")
print(f"app_name : {updated_session.app_name}")
print(f"user_id: {updated_session.user_id}")
print(f"state: {updated_session.state}")
events = updated_session.events
# print(events)
count = 0
for event in events:
    count = count + 1
    print(f"-------printing event {count} -----------")
    print(f"event content: {event.content}")
    print(f"event content role: {event.content.role}")
    print(f"event invocation_id: {event.invocation_id}")
    print(f"event author: {event.author}")
    print(f"event final response : {event.is_final_response()}")
    print(f"actions  actions : {event.actions}")
    print(f"actions  state_delta : {event.actions.state_delta}")

# root_agent = math_agent