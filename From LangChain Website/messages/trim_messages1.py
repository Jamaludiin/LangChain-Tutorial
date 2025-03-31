from langchain_core.messages import (
    AIMessage,
    HumanMessage,
    SystemMessage,
    trim_messages,
)

# Sample chat history
messages = [
    SystemMessage("You're a helpful assistant that answers questions briefly."),
    HumanMessage("What is LangChain?"),
    AIMessage("LangChain is a framework for developing applications powered by language models."),
    HumanMessage("How does trim_messages work?"),
    AIMessage("It trims a list of messages based on token count or message count."),
    HumanMessage("Can you show me an example?"),
]

# Example 1: Trim based on token count (approximate)
trimmed_by_tokens = trim_messages(
    messages,
    max_tokens=50,  # Limit the chat history to 50 tokens
    strategy="last",  # Keep the most recent messages
    token_counter=len,  # Approximate token count by message length
    start_on="human",  # Ensure the chat starts with a HumanMessage
    include_system=True,  # Keep the SystemMessage if it exists
    allow_partial=False,
)
print("Trimmed by tokens:", trimmed_by_tokens)

# Example 2: Trim based on message count
trimmed_by_count = trim_messages(
    messages,
    max_tokens=3,  # Keep the last 3 messages only
    strategy="last",
    token_counter=len,
    start_on="human",
    include_system=True,
    allow_partial=False,
)
print("Trimmed by count:", trimmed_by_count)

# Example 3: Custom token counter function
def simple_token_counter(messages):
    return sum(len(msg.content.split()) for msg in messages)

trimmed_custom = trim_messages(
    messages,
    max_tokens=10,  # Keep messages within 10 words total
    strategy="last",
    token_counter=simple_token_counter,
    include_system=True,
)
print("Trimmed with custom counter:", trimmed_custom)
