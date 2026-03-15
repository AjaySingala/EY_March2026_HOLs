# Naïve Prompt Workflow (Failure Example).

# Set env vars from config.py.
import sys
import os

# Add the folder path (use absolute or relative path)
folder_path = os.path.join(os.path.dirname(__file__), '../..')
sys.path.insert(0, folder_path)

import config

# Start.
from langchain_openai import ChatOpenAI
import re

llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0.8
)


def naive_ticket_classifier(ticket):

    prompt = f"""
You are a technical support assistant.

Analyze the support ticket and return your analysis.

Ticket:
{ticket}
"""

    response = llm.invoke(prompt)

    return response.content


def parse_output(text):

    category = re.search(r"Category:\s*(.*)", text)
    severity = re.search(r"Severity:\s*(.*)", text)

    if not category or not severity:
        raise ValueError("Could not parse LLM output!")

    return {
        "category": category.group(1),
        "severity": severity.group(1)
    }


if __name__ == "__main__":

    ticket = """
Customers report intermittent 504 errors when calling the payment API.
The issue occurs mostly during peak hours.
"""

    result = naive_ticket_classifier(ticket)

    print("\nLLM OUTPUT\n")
    print(result)

    print("\nAttempting to parse...\n")

    try:
        parsed = parse_output(result)
        print("Parsed result:", parsed)

    except Exception as e:
        print("⚠️ PIPELINE FAILURE:", e)
