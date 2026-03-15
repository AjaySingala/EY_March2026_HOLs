# Agentic Flow with LangGraph.

from typing import TypedDict
from langgraph.graph import StateGraph, END
from langchain_openai import ChatOpenAI
from langchain.tools import tool
from tools import check_api_logs, check_server_load


llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)
print("LLM Initialized: gpt-4o-mini")

class AgentState(TypedDict):
    question: str
    analysis: str
    result: str


def analyze_issue(state: AgentState):
    print("\nAnalyzing issue...")

    question = state["question"]
    # TODO: Create a prompt that tells the LLM to analyze the issue
    # and determine what system to inspect.
    # Then return the analysis. 
    # Include the 'question' variable in the prompt.
    prompt = # Fill this in

    # TODO: Invoke the LLM with the prompt and return the analysis.
    response = # invoke the LLM with the prompt

    return {"analysis": response.content}


def investigate_system(state: AgentState):
    print("\nInvestigating system...")

    logs = check_api_logs.invoke({"service": "payment-api"})
    load = check_server_load.invoke({"server": "server-1"})

    result = f"""
Investigation Findings

Logs:
{logs}

Server Load:
{load}
"""

    return {"result": result}


def generate_report(state: AgentState):
    print("\nGenerating report...")

    prompt = f"""
Create a troubleshooting report.

Issue:
{state["question"]}

Analysis:
{state["analysis"]}

Investigation:
{state["result"]}
"""

    response = llm.invoke(prompt)

    return {"result": response.content}

# LangGrpah Orchestrator.
def build_graph():
    print("\nBuilding Graph Agent...")

    builder = StateGraph(AgentState)

    # TODO: Add nodes for each function.

    # TODO: Set the entry point to the 'analyze_issue' function.

    # TODO: Define the edges between the nodes to create the flow of the agent.

    return builder.compile()
