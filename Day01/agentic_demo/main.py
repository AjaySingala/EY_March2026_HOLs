# Main Runner.

# Set env vars from config.py.
import sys
import os

# Add the folder path (use absolute or relative path)
folder_path = os.path.join(os.path.dirname(__file__), '../..')
sys.path.insert(0, folder_path)

import config

# Start.

from dotenv import load_dotenv
from graph_agent import build_graph

graph = build_graph()
print("\nExecuting Graph Agent...\n")

result = graph.invoke(
    {
        "question": "My API is returning intermittent 504 errors"
    }
)
print("\nGraph Agent Execution Complete.\n")

print("\nFINAL RESULT\n")
print(result["result"])