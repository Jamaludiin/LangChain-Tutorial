# not woeking

from typing import Iterable
from langchain_core.document_loaders.blob_loaders import BlobLoader
from langchain_core.documents.blob import Blob  # ✅ Correct Import

class SimpleBlobLoader(BlobLoader):
    """A custom BlobLoader that loads raw text content from a file."""

    def __init__(self, file_path: str) -> None:
        """Initialize the loader with the file path."""
        self.file_path = file_path

    def yield_blobs(self) -> Iterable[Blob]:
        """Reads the file and yields its raw content as a Blob."""
        with open(self.file_path, "r", encoding="utf-8") as file:
            content = file.read()
            yield Blob(data=content.encode("utf-8"), metadata={"source": self.file_path})

# --- Create a Test File ---
test_file = "test_blob.txt"
with open(test_file, "w", encoding="utf-8") as f:
    f.write("This is a test blob file.\n")
    f.write("It contains raw data for processing.\n")

# --- Use the Custom BlobLoader ---
loader = SimpleBlobLoader(test_file)

# Load and print blobs
for blob in loader.yield_blobs():
    print(f"Blob Data: {blob.data.decode('utf-8')}")
    print(f"Metadata: {blob.metadata}")
