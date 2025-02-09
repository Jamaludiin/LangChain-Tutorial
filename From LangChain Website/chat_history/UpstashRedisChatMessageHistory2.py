import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from langchain.chains import LLMChain
from langchain_community.chat_message_histories.upstash_redis import (
    UpstashRedisChatMessageHistory,
)
from langchain.prompts import (
    ChatPromptTemplate,
    MessagesPlaceholder,
)

# Load environment variables
load_dotenv()

# Fetch Redis credentials
URL = os.getenv("UPSTASH_REDIS_REST_URL")
TOKEN = os.getenv("UPSTASH_REDIS_REST_TOKEN")

if not URL or not TOKEN:
    raise ValueError("Missing Upstash Redis credentials. Check your .env file.")

# Initialize Redis-based message history
history = UpstashRedisChatMessageHistory(
    url=URL, token=TOKEN, ttl=500, session_id="chat1"
)

# Configure memory
memory = ConversationBufferMemory(
    memory_key="chat_history",
    return_messages=True,
    chat_memory=history,
)

# Configure model and prompt
model = ChatOpenAI(
    model="gpt-3.5-turbo",
    temperature=0.6
)

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a friendly AI assistant."),
    MessagesPlaceholder(variable_name="chat_history"),
    ("human", "{input}")
])

# Use the recommended pipeline
chain = prompt | model

# Test queries
q1 = { "input": "My name is Leon" }
resp1 = chain.invoke(q1)
print(resp1.content)

q2 = { "input": "What is my name?" }
resp2 = chain.invoke(q2)
print(resp2.content)
