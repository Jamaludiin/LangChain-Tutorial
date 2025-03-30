from langchain_core.messages import messages_from_dict

# Define messages as a list of dictionaries
messages_dict = [
    {"type": "human", "content": "Hello!"},
    {"type": "ai", "content": "Hi there! How can I assist you?"},
    {"type": "human", "content": "What is LangChain?"}
]

# Convert to BaseMessage objects
messages = messages_from_dict(messages_dict)

# Print the converted messages
for msg in messages:
    print(f"{msg.type}: {msg.content}")
