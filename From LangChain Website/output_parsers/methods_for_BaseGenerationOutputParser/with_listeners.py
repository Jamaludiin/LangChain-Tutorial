# ERROR
"""17. with_listeners() - Add Event Listeners for Debugging
This method monitors events and logs activity.
"""

from langchain_groq import ChatGroq

def listener(event):
    print("\n=== with_listeners() Event ===")
    print(f"Event received: {event}")

llm = ChatGroq(model="llama-3.3-70b-versatile").with_listeners([listener])

response = llm.invoke("Tell me a fun fact about space.")

print("\n=== with_listeners() Response ===")
print(response)
