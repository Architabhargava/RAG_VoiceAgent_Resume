# Resume RAG Voice Agent

A production-ready voice-enabled assistant that uses RAG (Retrieval-Augmented Generation) to answer questions about a user's resume.

## Features

- **Resume Ingestion**: Load PDF resumes, chunk them, and store embeddings in Supabase.
- **RAG Retrieval**: Search for relevant resume sections to answer user queries accurately.
- **Voice Interaction**: Speak to the assistant and receive spoken responses.
- **Interruption Support**: Real-time interruption handling using WebSocket streaming.
- **Conversation Memory**: Persistent chat history stored in Supabase.
- **MCP Tools**: Exposes resume search and memory tools via Model Context Protocol.

## Tech Stack

- **Backend**: FastAPI, LangChain
- **LLM**: OpenAI GPT-4o
- **Vector Database**: Supabase pgvector
- **STT**: OpenAI Whisper
- **TTS**: ElevenLabs
- **Environment**: python-dotenv

## Setup Instructions

### 1. Supabase Setup

You need a Supabase project with `pgvector` enabled. Run the following SQL in your Supabase SQL Editor:

```sql
-- Enable the pgvector extension to work with embeddings
create extension if not exists vector;

-- Create a table for resume documents
create table if not exists documents (
  id bigserial primary key,
  content text,
  metadata jsonb,
  embedding vector(1536)
);

-- Create a function for vector search
create or replace function match_documents (
  query_embedding vector(1536),
  match_threshold float,
  match_count int
)
returns table (
  id bigint,
  content text,
  metadata jsonb,
  similarity float
)
language plpgsql
as $$
begin
  return query
  select
    documents.id,
    documents.content,
    documents.metadata,
    1 - (documents.embedding <=> query_embedding) as similarity
  from documents
  where 1 - (documents.embedding <=> query_embedding) > match_threshold
  order by similarity desc
  limit match_count;
end;
$$;

-- Create a table for conversation memory
create table if not exists chat_history (
  id bigserial primary key,
  session_id uuid default gen_random_uuid(),
  role text,
  message text,
  created_at timestamp with time zone default now()
);
```

### 2. Installation

1. Clone the repository.
2. Install dependencies:
   ```bash
   pip install -r backend/requirements.txt
   ```

### 3. Configuration

Create a `.env` file in the root directory (use the provided template):

```env
OPENAI_API_KEY=your_openai_api_key
SUPABASE_URL=your_supabase_url
SUPABASE_SERVICE_KEY=your_supabase_service_key
ELEVENLABS_API_KEY=your_elevenlabs_api_key
```

### 4. Resume Ingestion

Place your resume PDF at `resume/resume.pdf` and run:

```bash
export PYTHONPATH=$PYTHONPATH:.
python backend/app/rag/ingest.py
```

### 5. Run the Backend

```bash
uvicorn backend.main:app --reload
```

## WebSocket Usage

Connect to the `/voice` endpoint:

- **URL**: `ws://localhost:8000/voice`
- **Input**: Send raw audio bytes (WAV/MP3/etc.)
- **Output**: Receive audio bytes (MP3) from the assistant.

Interruption handling is built-in. If you send new audio while the assistant is processing, the previous task will be cancelled.

## MCP Integration

The system exposes MCP tools via a SSE (Server-Sent Events) endpoint at `/mcp`. These tools can be integrated into other AI agents or tools.

### MCP Tools available:
- `resume_search(query: str)`: Search the resume for relevant information.
- `conversation_memory(session_id: str)`: Retrieve the conversation history for a specific session.

### Configuration for Claude Desktop:
To use these tools in Claude Desktop, add the following to your `claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "resume-agent": {
      "command": "python",
      "args": ["-m", "backend.main"],
      "env": {
        "OPENAI_API_KEY": "your_openai_api_key",
        "SUPABASE_URL": "your_supabase_url",
        "SUPABASE_SERVICE_KEY": "your_supabase_service_key"
      }
    }
  }
}
```

Or connect via the SSE endpoint if using an MCP-compatible client that supports remote servers:
- **SSE URL**: `http://localhost:8000/mcp/sse`

## Frontend

A basic push-to-talk frontend is provided in the `frontend/` directory. To use it:
1. Open `frontend/index.html` in your browser.
2. Ensure the backend is running (`uvicorn backend.main:app`).
3. Click and hold the "Push to Talk" button to speak, then release to send the audio to the agent.
