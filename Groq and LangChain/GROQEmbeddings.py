# is working after i used the HuggingFaceEmbeddings

# Import necessary libraries
from langchain_groq import ChatGroq  # For creating embeddings using Groq
from langchain.vectorstores import FAISS    # Vector store for similarity search
from langchain.document_loaders import TextLoader  # To load text documents
from langchain.text_splitter import CharacterTextSplitter  # To split text into chunks
from dotenv import load_dotenv  # To load environment variables
import os
from langchain_community.embeddings import HuggingFaceEmbeddings

from langchain_community.embeddings import HuggingFaceEmbeddings

# Load environment variables from .env file (contains GROQ_API_KEY)
load_dotenv()

def create_embeddings_demo():
    # Step 1: Initialize Groq Embeddings
    # This creates an embedding model instance that will convert text to vectors
    """ embeddings = HuggingFaceEmbeddings(
        groq_api_key=os.getenv("GROQ_API_KEY")
    )"""
    # Create embeddings using HuggingFace
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-mpnet-base-v2"
    )

    # Step 2: Create a sample text file for demonstration
    # In a real application, you might load existing documents instead
    with open("sample.txt", "w") as f:
        f.write("""This is a sample document about artificial intelligence.
                AI is transforming many industries including healthcare and finance.
                Machine learning is a subset of AI that focuses on training models with data.""")

    # Step 3: Load the document
    # TextLoader reads the content of the text file
    loader = TextLoader("sample.txt")
    documents = loader.load()

    # Step 4: Split text into smaller chunks
    # This is important for processing long texts and getting more precise results
    text_splitter = CharacterTextSplitter(
        separator= " ",
        chunk_size=20,    # Each chunk will be ~1000 characters
        chunk_overlap=2   # Overlap between chunks to maintain context
    )
    texts = text_splitter.split_documents(documents)

    print("\nSPLITED TEXT STARTS")
    print(texts)
    print("SPLITED TEXT ENDS")


    # Step 5: Create vector store
    # FAISS is an efficient similarity search library
    # This step converts all text chunks to embeddings and stores them
    db = FAISS.from_documents(texts, embeddings)

    # Step 6: Perform a similarity search
    # Define a query to search for similar content
    query = "What is machine learning?"
    # Find documents most similar to the query
    docs = db.similarity_search(query)

    # Step 7: Display results
    print("\nSearch Results for:", query)
    for doc in docs:
        print("\nContent:", doc.page_content)

# Step 8: Main execution block
if __name__ == "__main__":
    create_embeddings_demo()