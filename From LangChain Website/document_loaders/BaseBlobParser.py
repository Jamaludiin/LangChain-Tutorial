"""
Here's a complete example that demonstrates how to:

    Create a custom document parser using BaseBlobParser.
    Load a file as a Blob.
    Parse the file into documents line by line.
    Test the parser by running it.

Steps Covered:
    Install dependencies: pip install langchain-core
    Create a sample file.
    Implement a MyParser class using BaseBlobParser.
    Load and parse the file using Blob.
"""



import os
from typing import Iterator
from langchain_core.document_loaders import BaseBlobParser, Blob
from langchain_core.documents import Document

# Step 1: Create a sample file
file_path = "sample.txt"
with open(file_path, "w", encoding="utf-8") as f:
    f.write("Hello, this is line 1.\n")
    f.write("This is another line.\n")
    f.write("Final line in the document.")

# Step 2: Create a custom parser using BaseBlobParser
class MyParser(BaseBlobParser):
    """A simple parser that creates a document from each line of a file."""

    def lazy_parse(self, blob: Blob) -> Iterator[Document]:
        """Parse a blob into documents, one per line."""
        line_number = 0
        with blob.as_bytes_io() as f:
            for line in f:
                line_number += 1
                yield Document(
                    page_content=line.strip(),  # Remove extra spaces
                    metadata={"line_number": line_number, "source": blob.source},
                )

# Step 3: Load the file as a Blob
blob = Blob.from_path(file_path)

# Step 4: Initialize parser and parse the blob
parser = MyParser()
documents = list(parser.lazy_parse(blob))

# Step 5: Print results
for doc in documents:
    print(f"\nDocument {doc.metadata['line_number']}:")
    print(f"Content: {doc.page_content}")
    print(f"Metadata: {doc.metadata}")

# Cleanup: Remove the sample file after testing
os.remove(file_path)


"""
How It Works:
The script creates a sample file (sample.txt) with 3 lines.
MyParser extends BaseBlobParser, reading each line and turning it into a Document object.
It loads the file as a Blob and parses it.
Finally, it prints the parsed documents with metadata.
This is a simple and fully functional example that you can run in one go. 🚀 Let me know if you need modifications!
"""