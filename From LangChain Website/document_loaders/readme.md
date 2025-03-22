What is BaseBlobParser?
Think of BaseBlobParser as a tool for extracting text from files (or other data sources) and converting it into documents that a language model can understand.

For example, if you have a text file with multiple lines, you can use BaseBlobParser to break it into separate documents, each containing one line.

Simple Example
We’ll create a custom parser that reads a text file and converts each line into a Document.

Step 1: Import necessary modules
python
Copy
Edit
from typing import Iterator
from langchain_core.document_loaders import BaseBlobParser, Blob
from langchain_core.documents import Document
Step 2: Create a custom parser
python
Copy
Edit
class SimpleTextParser(BaseBlobParser):
    """A simple parser that creates a document from each line."""

    def lazy_parse(self, blob: Blob) -> Iterator[Document]:
        """Parse a blob into separate documents, one per line."""
        with blob.as_bytes_io() as f:
            for line_number, line in enumerate(f, start=1):
                yield Document(
                    page_content=line.strip(),  # Remove extra spaces/newlines
                    metadata={"line_number": line_number, "source": blob.source},
                )
Step 3: Use the parser
python
Copy
Edit
# Create a blob from a file
blob = Blob.from_path("example.txt")

# Create an instance of our parser
parser = SimpleTextParser()

# Parse the file
documents = list(parser.lazy_parse(blob))

# Print the parsed documents
for doc in documents:
    print(doc)
Example Input (example.txt)
pgsql


Hello, this is line 1.
This is another line.
Final line here!
Example Output

Document(page_content='Hello, this is line 1.', metadata={'line_number': 1, 'source': 'example.txt'})
Document(page_content='This is another line.', metadata={'line_number': 2, 'source': 'example.txt'})
Document(page_content='Final line here!', metadata={'line_number': 3, 'source': 'example.txt'})
Key Takeaways
✔ BaseBlobParser helps convert files into structured documents.
✔ lazy_parse(blob) reads data line by line, making it memory efficient.
✔ Each Document contains text (page_content) + metadata (e.g., line number, file name).

Would you like an even simpler example or one using data stored in memory? 🚀



Why Use BaseBlobParser?
BaseBlobParser is part of the LangChain framework and is designed for parsing unstructured data from binary blobs (e.g., text files, PDFs, JSON, HTML, etc.). It provides a structured way to extract meaningful documents from raw file data.

Key Reasons to Use BaseBlobParser
1. Works with Blob Objects
Blob represents raw file data and can handle different file types.
BaseBlobParser allows parsing these blobs efficiently.
2. Streamlined Document Extraction
BaseBlobParser implements lazy_parse(), which allows streaming documents instead of loading everything at once.
This is useful for handling large files without consuming too much memory.
3. Metadata Handling
It allows you to add metadata (e.g., file name, page number, line number) to documents.
This helps in document indexing and retrieval.
4. Custom Parsing Logic
You can define your own rules for extracting data from files.
Works well for structured and unstructured text.
Example Use Case
If you have a large text file with logs or CSV-like data, BaseBlobParser allows you to process each line as a separate document without loading everything into memory.

from typing import Iterator
from langchain_core.document_loaders import BaseBlobParser, Blob
from langchain_core.documents import Document

class LogFileParser(BaseBlobParser):
    """Parser that extracts each log entry as a separate document."""
    
    def lazy_parse(self, blob: Blob) -> Iterator[Document]:
        with blob.as_bytes_io() as f:
            for line in f:
                yield Document(
                    page_content=line.strip(),
                    metadata={"source": blob.source}
                )

# Load a log file and parse it
blob = Blob.from_path("server.log")
parser = LogFileParser()
documents = list(parser.lazy_parse(blob))

# Print the parsed documents
for doc in documents:
    print(doc.page_content, doc.metadata)
