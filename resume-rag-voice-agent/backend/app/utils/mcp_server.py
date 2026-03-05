from mcp.server.fastmcp import FastMCP
from backend.app.rag.retriever import search_resume
from backend.app.memory.store import SupabaseChatMemory

# Initialize MCP server using FastMCP
mcp = FastMCP("ResumeVoiceAgentTools")

@mcp.tool()
async def resume_search(query: str) -> str:
    """
    Search the resume for relevant information based on a query.
    """
    docs = search_resume(query)
    return "\n\n".join([doc.page_content for doc in docs])

@mcp.tool()
async def conversation_memory(session_id: str) -> str:
    """
    Retrieve the conversation memory for a specific session.
    """
    memory = SupabaseChatMemory(session_id)
    history = memory.get_messages()

    formatted_history = ""
    for msg in history:
        formatted_history += f"{msg['role'].capitalize()}: {msg['message']}\n"

    return formatted_history if formatted_history else "No history found for this session."
