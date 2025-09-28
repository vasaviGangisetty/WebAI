import streamlit as st
from backend import search_web, summarize_html
import streamlit.components.v1 as components

st.set_page_config(page_title="WebAi Viewer", layout="wide")

st.title("🌐 Live Web Page Viewer")

query = st.text_input("Enter your query:")

# Buttons
col1, col2 = st.columns(2)
summarize_mode = False
with col1:
    search_btn = st.button("🔎 Search")
with col2:
    summarize_btn = st.button("📝 Summarize")

if query and (search_btn or summarize_btn):
    result = search_web(query)
    if "error" in result:
        st.error(result["error"])
    else:
        if summarize_btn:
            st.subheader("Summary")
            st.write(summarize_html(result['html']))
        else:
            st.subheader("Full Web Page")
            components.html(result['html'], height=800, scrolling=True)
