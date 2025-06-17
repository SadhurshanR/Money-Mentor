# 💸 Money Mentor – AI-Powered Financial Agent

**Money Mentor** is a personalized AI financial assistant designed to help users make smarter money decisions. It answers financial questions, provides budgeting tips, and explains investment concepts—all through natural language conversations. Ideal for students and young adults seeking accessible, trustworthy financial guidance.

---

## 🚀 Features

- 🧠 Uses the **ReAct agent pattern** for reasoning and action-taking
- ⚡ Fast and reliable responses powered by **Groq’s LLaMA 3**
- 🔎 Real-time search via **Tavily API** for up-to-date information
- 🖥 User-friendly interface built with **Streamlit**
- 📄 Automatically saves conversation history as `.txt` files

---

## 🧠 How the Agent Works

Money Mentor follows the **ReAct (Reason + Act)** agent pattern, where the AI agent:

1. **Reasons** about the user’s question using its internal knowledge
2. **Acts** by deciding whether to take a tool-based action—like searching the web
3. **Observes** the result (e.g., from Tavily Search)
4. **Thinks** again and continues reasoning
5. **Responds** with a final, fact-based answer

This cycle allows the agent to combine both **tool usage (action)** and **LLM reasoning** to produce accurate and useful financial advice.

---

## 🛠️ Tech Stack

- **Python** – Core language for development
- **LangGraph** – Framework to orchestrate agent logic
- **Groq (LLaMA 3)** – Large Language Model provider
- **Tavily API** – Real-time web search for external data
- **Streamlit** – Lightweight UI framework for quick deployment
- **python-dotenv** – To manage API keys securely using `.env` file

---

## 📦 Required Dependencies

Included in `requirements.txt`:

