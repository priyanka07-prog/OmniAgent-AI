from Multibot.Streamlit_app import response
from langchain.agent import initialize_agent
from langchain.tools import Tool
from bots.research_bot import research_bot
from bots.rag_bot import rag_bot 

tools = [
    Tool(
        name="Research Bot",
        func=research_bot,
        description="Use for web search"
    ),
    Tool(
        name="RAG Bot",
        func=rag_bot,
        description="Use for retrieval-augmented generation"
    )
]

def run_agent(query):
    
    agent = initialize_agent(
        tools,
        llm = None,
        agent="zero-shot-react-description",
        verbose=True
    )
    
    response = agent.run(query)
    
    return response