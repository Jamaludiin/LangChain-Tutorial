from typing import Iterator
from langchain_core.document_loaders import BaseLoader
from langchain_core.documents import Document

class SimpleTextLoader(BaseLoader):
    """A custom document loader that reads a text file line by line."""

    def __init__(self, file_path: str) -> None:
        """Initialize the loader with the file path."""
        self.file_path = file_path

    def lazy_load(self) -> Iterator[Document]:
        """Reads the file and yields each line as a separate document."""
        with open(self.file_path, "r", encoding="utf-8") as file:
            for line_number, line in enumerate(file):
                yield Document(
                    page_content=line.strip(),
                    metadata={"line_number": line_number, "source": self.file_path}
                )

# --- Create a Test File ---
test_file = "test.txt"
with open(test_file, "w", encoding="utf-8") as f:
    f.write("Hello, world!\n")
    f.write("This is a simple test file.\n")
    f.write("LangChain makes document processing easy!\n")

# --- Use the Custom Loader ---
loader = SimpleTextLoader(test_file)

# Load and print documents
for doc in loader.lazy_load():
    print(doc)
