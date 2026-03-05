from fastapi import FastAPI
from backend.app.api.voice_api import router as voice_router
from backend.app.utils.mcp_server import mcp
from dotenv import load_dotenv
import uvicorn

load_dotenv()

app = FastAPI(title="Resume RAG Voice Agent")

# Include the voice API router
app.include_router(voice_router)

# Mount MCP server SSE app
app.mount("/mcp", mcp.sse_app())

@app.get("/")
async def root():
    return {"message": "Resume RAG Voice Agent API is running"}

if __name__ == "__main__":
    uvicorn.run("backend.main:app", host="0.0.0.0", port=8000, reload=True)
