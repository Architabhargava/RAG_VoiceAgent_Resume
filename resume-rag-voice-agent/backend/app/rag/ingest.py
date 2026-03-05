import os
from dotenv import load_dotenv
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import SupabaseVectorStore
from backend.app.utils.supabase_client import get_supabase_client

load_dotenv()

def ingest_resume(file_path: str):
    """
    Loads a resume PDF, splits it into chunks, generates embeddings,
    and stores them in Supabase pgvector.
    """
    if not os.path.exists(file_path):
        print(f"File not found: {file_path}")
        return

    print(f"Loading resume from {file_path}...")
    loader = PyPDFLoader(file_path)
    documents = loader.load()

    print("Splitting text into chunks...")
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=100
    )
    docs = text_splitter.split_documents(documents)

    print("Generating embeddings and storing in Supabase...")
    embeddings = OpenAIEmbeddings()
    supabase = get_supabase_client()

    SupabaseVectorStore.from_documents(
        docs,
        embeddings,
        client=supabase,
        table_name="documents",
        query_name="match_documents",
    )

    print("Ingestion complete.")

if __name__ == "__main__":
    resume_path = os.path.join(os.path.dirname(__file__), "../../../resume/resume.pdf")
    ingest_resume(resume_path)
