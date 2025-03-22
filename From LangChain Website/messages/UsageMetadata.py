from langchain_core.messages.ai import UsageMetadata
# static simple example but no AI
# Example usage metadata for a chat message
usage_data = UsageMetadata(
    input_tokens=10,  # Tokens used for the question
    output_tokens=8,   # Tokens used for the response
    total_tokens=18,   # Total tokens used
    input_token_details={
        "cache_read": 5,  # Tokens retrieved from cache
        "audio": 2,       # Tokens used for audio processing (if applicable)
    },
    output_token_details={
        "reasoning": 6,  # Tokens used for logical reasoning in response
    }
)

# Print the usage data
print(usage_data)
