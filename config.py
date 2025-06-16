import uuid

# MODEL = "gemini-2.5-flash-preview-05-20"
MODEL ="gemini-2.0-flash"
APP_NAME = "Code reviewer"
USER_ID = "user" +  str(uuid.uuid4())[:8]
SESSION_ID = "session_001" + str(uuid.uuid4())[:8]
