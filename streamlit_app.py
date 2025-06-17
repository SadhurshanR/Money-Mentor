import os
import textwrap
import streamlit as st
from dotenv import load_dotenv
from langgraph.prebuilt import create_react_agent
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_openai import ChatOpenAI

# --- Load environment variables ---
load_dotenv()

# --- Agent Setup ---
search_tool = TavilySearchResults()

llm = ChatOpenAI(
    openai_api_key=os.getenv("GROQ_API_KEY"),
    openai_api_base="https://api.groq.com/openai/v1",
    model="llama3-70b-8192",
    temperature=0
)

agent_executor = create_react_agent(llm, tools=[search_tool])

# --- Streamlit UI Config ---
st.set_page_config(page_title="Money Mentor", page_icon="💰", layout="centered")
st.markdown(
    """
    <style>
    body {
        background: linear-gradient(to right, #0f2027, #203a43, #2c5364);
        color: #f0f0f0;
    }
    .reportview-container {
        background-color: transparent;
    }
    .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
    }
    .stTextInput > div > div > input {
        background-color: #ffffff;
        color: black;
        font-size: 16px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# --- Title ---
st.markdown(
    "<h1 style='text-align: center; color: #FCD34D;'>💰 Money Mentor</h1>", unsafe_allow_html=True)
st.markdown(
    "<h4 style='text-align: center; color: #d1d5db;'>Your AI Financial Advisor</h4>", unsafe_allow_html=True)

# --- Input ---
with st.form(key="qa_form"):
    question = st.text_area("💬 Ask a financial question:", height=100, placeholder="e.g., Is Tesla a good investment in 2025?")
    submit = st.form_submit_button("🔎 Ask")

if submit and question:
    with st.spinner("Money Mentor is thinking..."):
        try:
            response = agent_executor.invoke({
                "messages": [{"role": "user", "content": question}]
            })

            if isinstance(response, dict) and "messages" in response:
                final_answer = response["messages"][-1].content
            elif hasattr(response, "content"):
                final_answer = response.content
            else:
                final_answer = "⚠️ Could not extract the final message."

            clean_text = final_answer.replace("\n", " ").strip()
            wrapped = textwrap.fill(clean_text, width=100)

            # --- Output ---
            st.markdown("### 💡 Money Mentor's Answer:")
            st.success(wrapped)

            # --- Logging ---
            with open("money_mentor_log.txt", "a", encoding="utf-8") as log_file:
                log_file.write(f"Q: {question}\nA: {clean_text}\n{'-'*80}\n")

        except Exception as e:
            st.error(f"⚠️ Agent failed to respond: {e}")
