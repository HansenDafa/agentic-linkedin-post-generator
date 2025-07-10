# app.py

import streamlit as st
import pandas as pd
from multi_agent import multi_agent_pipeline

st.title("🧠 Agentic LinkedIn Post Generator")
st.caption("Powered by LLaMA3 + ReAct-style iteration via Ollama")

uploaded_file = st.file_uploader("Upload your `achievements.csv`", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    entries = df.to_dict(orient='records')

    selected_idx = st.selectbox("Choose an entry:", range(len(entries)), format_func=lambda i: entries[i]['Title'])
    style = st.selectbox("Choose tone style:", ["inspirational", "funny", "concise", "professional"])


if st.button("Run Multi-Agent Generator"):
    with st.spinner("Agents are collaborating..."):
        result = multi_agent_pipeline(entries[selected_idx], style=style)

    with st.expander("🧠 Agent Logs"):
        for step in result['log']:
            st.markdown(f"- {step}")
        

    st.subheader("🚀 Final LinkedIn Post")
    st.success(result['final'])
