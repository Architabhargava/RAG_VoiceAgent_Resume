from typing import List
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from backend.app.rag.retriever import get_retriever
from backend.app.memory.store import SupabaseChatMemory

class ResumeAgent:
    """
    An agent that answers questions about a resume using RAG and maintains conversation history.
    """
    def __init__(self, session_id: str):
        self.session_id = session_id
        self.llm = ChatOpenAI(model="gpt-4o", temperature=0)
        self.retriever = get_retriever()
        self.memory = SupabaseChatMemory(session_id)

        self.system_prompt = """
        You are a helpful Resume Assistant. You answer questions about a user's resume using the provided context.
        If the information is not in the resume, say you don't know based on the resume.
        Keep your answers concise and professional as they will be spoken.
        """

    async def answer_question(self, query: str) -> str:
        """
        Retrieves context, constructs a prompt, and generates an answer.
        """
        # 1. Retrieve context
        docs = self.retriever.invoke(query)
        context = "\n\n".join([doc.page_content for doc in docs])

        # 2. Get chat history
        history = self.memory.get_messages()

        # 3. Construct messages
        messages = [SystemMessage(content=self.system_prompt)]

        # Add history
        for msg in history:
            if msg["role"] == "user":
                messages.append(HumanMessage(content=msg["message"]))
            else:
                messages.append(AIMessage(content=msg["message"]))

        # Add current context and query
        human_content = f"Context from resume:\n{context}\n\nQuestion: {query}"
        messages.append(HumanMessage(content=human_content))

        # 4. Generate response
        response = await self.llm.ainvoke(messages)
        answer = response.content

        # 5. Store in memory
        self.memory.add_message("user", query)
        self.memory.add_message("assistant", answer)

        return answer
