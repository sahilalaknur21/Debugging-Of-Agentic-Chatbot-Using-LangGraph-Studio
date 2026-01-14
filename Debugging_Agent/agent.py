from typing import Annotated, TypedDict
from langchain_groq import ChatGroq
from langgraph.graph import END, START, StateGraph
from langgraph.graph.message import add_messages
from langgraph.prebuilt import ToolNode, tools_condition
from langchain_core.messages import BaseMessage, HumanMessage
from langchain_community.tools import ArxivQueryRun, WikipediaQueryRun
from langchain_community.utilities import ArxivAPIWrapper, WikipediaAPIWrapper
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_core.tools import tool
from langgraph.checkpoint.memory import MemorySaver
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

os.environ["GROQ_API_KEY"]=os.getenv("GROQ_API_KEY")
os.environ["LANGSMITH_API_KEY"]=os.getenv("LANGSMITH_API_KEY")

# --- 1. Define Tools ---

# Arxiv
api_wrapper_arxiv = ArxivAPIWrapper(top_k_results=2, doc_content_chars_max=500)
arxiv = ArxivQueryRun(api_wrapper=api_wrapper_arxiv)

# Wikipedia
api_wrapper_wiki = WikipediaAPIWrapper(top_k_results=1, doc_content_chars_max=500)
wiki = WikipediaQueryRun(api_wrapper=api_wrapper_wiki)

# Tavily
tavily = TavilySearchResults()

# Custom Math Tools
@tool
def multiply(a: int, b: int) -> int:
    """Multiplies two integers and returns the result."""
    return a * b

@tool
def add(a: int, b: int) -> int:
    """Adds two integers and returns the result."""
    return a + b

@tool
def divide(a: int, b: int) -> float:
    """Divides the first integer by the second and returns the result."""
    if b == 0:
        return "Error: Cannot divide by zero."
    return a / b

# Combine all tools
tools = [arxiv, wiki, tavily, multiply, add, divide]

# --- 2. Define State ---
class State(TypedDict):
    messages: Annotated[list[BaseMessage], add_messages]

# --- 3. Initialize LLM ---
# Using Groq as per your notebook
llm = ChatGroq(model="qwen/qwen3-32b", temperature=0)
llm_with_tools = llm.bind_tools(tools)

# --- 4. Define Nodes ---

def tool_calling_llm(state: State):
    """
    The main reasoning node.
    """
    messages = state["messages"]
    response = llm_with_tools.invoke(messages)
    return {"messages": [response]}

# --- 5. Build Graph ---
builder = StateGraph(State)

# Add Nodes
builder.add_node("tool_calling_llm", tool_calling_llm)
builder.add_node("tools", ToolNode(tools))

# Add Edges
builder.add_edge(START, "tool_calling_llm")

builder.add_conditional_edges(
    "tool_calling_llm",
    # If the LLM requests a tool -> go to "tools"
    # If the LLM responds with text -> go to END
    tools_condition,
)

# Return from tools back to LLM (Cyclical/ReAct pattern)
builder.add_edge("tools", "tool_calling_llm")

# --- 6. Compile & Export ---
# Adding MemorySaver for persistence
memory = MemorySaver()
graph = builder.compile()