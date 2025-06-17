# 💸 Money Mentor – AI-Powered Financial Agent

Money Mentor is a personalized AI financial assistant designed to help users make smarter money decisions. It uses a large language model agent to answer financial questions, assist with budgeting, and provide investment tips through a natural and conversational interface. This tool is ideal for students and young adults who want accessible, reliable financial guidance.

 🚀 Features

- 🧠 Multi-agent architecture using LangGraph for structured task flow
- ⚡ Powered by Groq’s ultra-fast LLaMA 3 for intelligent responses
- 🔎 Real-time information retrieval through Tavily Search
- 🖥 Built with Streamlit for a clean and interactive user interface
- 📄 Saves user conversations to `.txt` for future reference


 🤖 Agent Type

Money Mentor is built using a **multi-agent framework** with LangGraph. The agent operates in a workflow that includes:

- **Search Agent** – fetches real-time data using Tavily  
- **Answer Agent** – processes the user query using LLM reasoning  
- **Controller** – orchestrates the flow between components to return accurate and reliable answers

---

## 🛠️ Tech Stack

- **Python** – Core development language
- **LangGraph** – Multi-agent workflow orchestration
- **Groq (LLaMA 3)** – Large Language Model backend
- **Tavily API** – Real-time search augmentation
- **Streamlit** – Web UI for user interaction
- **dotenv** – Environment variable management for API keys

---

## 📦 Required Dependencies

Add these to your `requirements.txt`:

