import os
import streamlit as st

def get_gemini_key():
    # Prefer Streamlit Secrets; fall back to env vars; accept either name
    return ( 
        os.getenv("GOOGLE_API_KEY")
    )

API_KEY = (get_gemini_key() or "").strip()
st.write("Key loaded:", bool(API_KEY))
if not API_KEY:
    st.error("No API key found. Add GEMINI_API_KEY (or GOOGLE_API_KEY) to Streamlit secrets or env.")
    st.stop()

