from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import SupabaseVectorStore
from backend.app.utils.supabase_client import get_supabase_client

def get_retriever():
    """
    Returns a LangChain retriever that searches Supabase using pgvector similarity.
    """
    supabase = get_supabase_client()
    embeddings = OpenAIEmbeddings()

    vector_store = SupabaseVectorStore(
        client=supabase,
        embedding=embeddings,
        table_name="documents",
        query_name="match_documents",
    )

    return vector_store.as_retriever(search_kwargs={"k": 5})

def search_resume(query: str):
    """
    Embeds the query and searches Supabase for the most relevant resume chunks.
    """
    retriever = get_retriever()
    relevant_docs = retriever.invoke(query)
    return relevant_docs
