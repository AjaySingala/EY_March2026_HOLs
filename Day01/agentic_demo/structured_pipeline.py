# Structured Output with JSON Schema.

# Set env vars from config.py.
import sys
import os

# Add the folder path (use absolute or relative path)
folder_path = os.path.join(os.path.dirname(__file__), '../..')
sys.path.insert(0, folder_path)

import config

# Start.
from langchain_openai import ChatOpenAI
from pydantic import BaseModel, Field

class TroubleshootingOutput(BaseModel):
    category: str = Field(description="Type of issue")
    severity: str = Field(description="low, medium, high")
    steps: list[str] = Field(description="Troubleshooting steps")


llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

# TODO: Bind the LLM to the TroubleshootingOutput schema
structured_llm = # Fill this in

def structured_pipeline(question: str):
    # TODO: Create a prompt that tells the LLM it is a DevOps assistant
    # and includes the 'question' variable.
    prompt = # Fill this in
    
    response = structured_llm.invoke(prompt)
    return response


if __name__ == "__main__":
    q = "My API is returning intermittent 504 timeouts"
    result = structured_pipeline(q)

    print(result.model_dump_json(indent=2))
