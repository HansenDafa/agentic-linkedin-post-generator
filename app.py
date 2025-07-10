# app.py

import streamlit as st
import pandas as pd
from react_agent import react_agent

st.title("🧠 Agentic LinkedIn Post Generator")
st.caption("Powered by LLaMA3 + ReAct-style iteration via Ollama")

uploaded_file = st.file_uploader("Upload your `achievements.csv`", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    entries = df.to_dict(orient='records')

    selected_idx = st.selectbox("Choose an entry:", range(len(entries)), format_func=lambda i: entries[i]['Title'])

    if st.button("Generate LinkedIn Post"):
        with st.spinner("Reasoning, generating, critiquing..."):
            result = react_agent(entries[selected_idx])

        with st.expander("🧠 Agent Reasoning"):
            for step in result['reasoning']:
                st.markdown(f"- {step}")
        
        st.subheader("📝 Initial Draft")
        st.write(result['draft'])

        st.subheader("🔍 Critique Feedback")
        st.write(result['feedback'])

        st.subheader("✅ Final Refined Post")
        st.success(result['refined'])
