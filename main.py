from typing_extensions import TypedDict
from langchain.chat_models import init_chat_model
from langgraph.graph import StateGraph, START, END
from dotenv import load_dotenv
import os
import json

load_dotenv()
os.environ["GOOGLE_API_KEY"] = os.getenv("GEMINI_API_KEY")

llm = init_chat_model("gemini-2.0-flash-lite", model_provider="google-genai")

class State(TypedDict):
    messages: list

def chatbot(state: State) -> State:
    return {"messages": [*state["messages"], llm.invoke(state["messages"])]}

# Build the LangGraph state machine
builder = StateGraph(State)
builder.add_node("chatbot_node", chatbot)
builder.add_edge(START, "chatbot_node")
builder.add_edge("chatbot_node", END)
graph = builder.compile()

# Load log.json if it exists
log_file_path = 'log.json'
conversation_log = []
if os.path.exists(log_file_path):
    with open(log_file_path, 'r') as file:
        try:
            data = json.load(file)
            if isinstance(data, list):
                conversation_log = data
            else:
                print("log.json is not a list. Overwriting with a new list.")
        except json.JSONDecodeError:
            print(" log.json is corrupted. Starting fresh.")

# Memory of full chat messages
chat_memory = []

print("🤖 Gemini Chatbot (type 'exit' to quit)\n")

while True:
    user_input = input("You: ")
    if user_input.lower() in ['exit', 'quit']:
        print("Exiting chat.")
        break

    # Append user message to memory
    chat_memory.append({"role": "user", "content": user_input})

    # Invoke the graph with current memory
    result = graph.invoke({"messages": chat_memory})
    ai_response = result["messages"][-1].content

    # Append AI message to memory
    chat_memory.append({"role": "assistant", "content": ai_response})

    # Show response
    print(f"Gemini: {ai_response}\n")

    # Log conversation turn
    conversation_log.append({
        "input": user_input,
        "output": ai_response
    })

    # Save updated log to file
    with open(log_file_path, 'w') as file:
        json.dump(conversation_log, file, indent=4)
