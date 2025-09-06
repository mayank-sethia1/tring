import os
import streamlit as st
import google.generativeai as genai

def get_gemini_key():
    # Prefer Streamlit Secrets; fall back to env vars; accept either name
    return (
        st.secrets.get("GEMINI_API_KEY")
        or os.getenv("GEMINI_API_KEY")
        or st.secrets.get("GOOGLE_API_KEY")
        or os.getenv("GOOGLE_API_KEY")
    )

API_KEY = (get_gemini_key() or "").strip()

if not API_KEY:
    st.error("No API key found. Add GEMINI_API_KEY (or GOOGLE_API_KEY) to Streamlit secrets or env.")
    st.stop()

genai.configure(api_key=API_KEY)
