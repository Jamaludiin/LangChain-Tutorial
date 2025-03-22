from typing import Iterator
from langchain_core.document_loaders import BaseLoader
from langchain_core.documents import Document

class SimpleFileLoader(BaseLoader):
    """A basic document loader that reads a file line by line."""

    def __init__(self, file_path: str) -> None:
        """Initialize the loader with a file path.

        Args:
            file_path: The path to the file to load.
        """
        self.file_path = file_path

    def lazy_load(self) -> Iterator[Document]:  
        """Lazily load documents, one per line."""
        with open(self.file_path, "r", encoding="utf-8") as f:
            for line_number, line in enumerate(f):
                yield Document(
                    page_content=line.strip(), 
                    metadata={"line_number": line_number, "source": self.file_path}
                )

# Create a test file
with open("test_file.txt", "w", encoding="utf-8") as f:
    f.write("Hello, this is the first line.\n")
    f.write("This is the second line.\n")
    f.write("And here is the third line.\n")

# Load the file using our custom loader
loader = SimpleFileLoader("test_file.txt")

# Iterate over the loaded documents
for doc in loader.lazy_load():
    print(doc)

