import os
from dotenv import load_dotenv
import textwrap

# --- Styling for terminal output ---
class Style:
    BOLD = "\033[1m"
    RESET = "\033[0m"
    GREEN = "\033[92m"
    BLUE = "\033[94m"
    CYAN = "\033[96m"
    YELLOW = "\033[93m"

# === Load API Keys ===
load_dotenv()

print("Groq (LLaMA3-70B):", os.getenv("GROQ_API_KEY"))
print("Tavily:", os.getenv("TAVILY_API_KEY"))

# === Agent Setup ===
from langgraph.prebuilt import create_react_agent
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_openai import ChatOpenAI

search_tool = TavilySearchResults()

llm = ChatOpenAI(
    openai_api_key=os.getenv("GROQ_API_KEY"),
    openai_api_base="https://api.groq.com/openai/v1",
    model="llama3-70b-8192",
    temperature=0
)

agent_executor = create_react_agent(llm, tools=[search_tool])

# === Ask question via input ===
question = input("\n💬 What financial question would you like to ask Money Mentor?\n> ")

# === Run agent with error handling ===
try:
    response = agent_executor.invoke({
        "messages": [{"role": "user", "content": question}]
    })

    print(f"\n{Style.BOLD}{Style.CYAN}💡 Money Mentor's Insight:{Style.RESET}\n")

    if isinstance(response, dict) and "messages" in response:
        final_answer = response["messages"][-1].content
    elif hasattr(response, "content"):
        final_answer = response.content
    else:
        final_answer = None

    if final_answer:
        clean_text = final_answer.replace("\n", " ").strip()
        print(textwrap.fill(clean_text, width=100))

        # ✅ Save to .txt log
        with open("money_mentor_log.txt", "a", encoding="utf-8") as log_file:
            log_file.write(f"Q: {question}\nA: {clean_text}\n{'-'*80}\n")
    else:
        print(f"{Style.YELLOW}⚠️ Could not extract a response from the agent.{Style.RESET}")

except Exception as e:
    print(f"{Style.YELLOW}⚠️ Agent failed to respond: {e}{Style.RESET}")
