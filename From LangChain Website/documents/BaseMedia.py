# not woeking

from langchain_core.documents.base import BaseMedia
from pydantic import Field

# Define a custom media class (inheriting from BaseMedia)
class TextMedia(BaseMedia):
    content: str = Field(..., description="The text content of the media")  # Declare the content as a field
    
    def __init__(self, content: str, media_id: str = None, metadata: dict = None):
        # First set the content
        self.content = content
        # Then initialize the parent class
        super().__init__(id=media_id, metadata=metadata)
    
    def __repr__(self):
        return f"TextMedia(id={self.id}, metadata={self.metadata}, content={self.content})"

# Example usage
if __name__ == "__main__":
    # Define media content (a simple text document)
    text_content = "This is a sample text document."
    media_metadata = {
        "author": "John Doe",
        "category": "Text Document",
        "created_at": "2025-02-10"
    }

    # Create an instance of TextMedia and pass content, media_id, and metadata
    media = TextMedia(content=text_content, media_id="123e4567-e89b-12d3-a456-426614174000", metadata=media_metadata)

    # Display media content and metadata
    print("Media Content:")
    print(media.content)
    print("\nMetadata:")
    print(media.metadata)

    # You can also access the unique ID
    print("\nMedia ID:")
    print(media.id)
