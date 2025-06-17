# 💰 Money Mentor – Your AI Financial Advisor

**Money Mentor** is an interactive, agentic AI system built using [LangGraph](https://github.com/langchain-ai/langgraph), [LLaMA 3 (Groq)](https://console.groq.com/), and [Tavily Search](https://www.tavily.com/) to provide real-time financial insights based on live web data.

This project demonstrates a fully functioning **ReAct-style AI agent** that can:
- 🔍 Perform live financial research
- 🧠 Reason over real-time search results
- 💡 Deliver intelligent investment insights
- 💬 Interact via command line or web UI (Streamlit)

---

## 🚀 Live Demo (Optional)

> 💡 Coming soon: [Streamlit Cloud Link Here]

---

## 🛠️ Tech Stack

| Component | Purpose |
|----------|---------|
| 🧠 LLaMA 3-70B via Groq | Fast, open-source LLM for reasoning |
| 🔎 Tavily Search API | Fetches up-to-date web search results |
| 🕸️ LangGraph | ReAct-style agent flow (reason-act-observe) |
| 🌐 Streamlit | Interactive web interface |
| 🐍 Python | Base language for agent orchestration |
| 🔐 dotenv | API key management |

---

## ✨ Features

- ✅ ReAct-style agent with LangGraph
- ✅ Real-time search with Tavily
- ✅ Clean, professional CLI and Streamlit UI
- ✅ Robust error handling
- ✅ Logs questions and answers to `money_mentor_log.txt`

---

## 📸 UI Preview

![Money Mentor UI](assets/money_mentor_ui.png) <!-- Replace with your screenshot path -->

---

## 💬 Example Questions

- Is Tesla a good investment in 2025?
- Should I invest in gold or bitcoin this year?
- Compare Apple and Microsoft as long-term investments
- What are the latest EV market trends?

---

## 🧪 Agent Evaluation

| Criteria | Result |
|---------|--------|
| 🔍 Uses tools effectively | ✅ |
| 🧠 Provides clear reasoning | ✅ |
| 💡 Handles ambiguity | ✅ |
| ❗ Graceful failure handling | ✅ |
| 📊 Answers are well-structured | ✅ |

---

## ⚙️ Setup Instructions

### 1. Clone this repo
```bash
git clone https://github.com/your-username/money-mentor.git
cd money-mentor
