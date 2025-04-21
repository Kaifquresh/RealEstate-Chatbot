import streamlit as st
from rag import generate_answer, process_urls

# Page config
st.set_page_config(page_title="Smart URL Bot", page_icon="🤖", layout="centered")

# Title
st.markdown("<h1 style='text-align: center; color: #4B8BBE;'>🤖 Smart URL Bot</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: grey;'>Ask questions based on content from your favorite URLs</p>", unsafe_allow_html=True)
st.markdown("---")

# Sidebar
st.sidebar.header("🔗 Enter URLs to Process")
url1 = st.sidebar.text_input('🔗 URL 1')
url2 = st.sidebar.text_input('🔗 URL 2')
url3 = st.sidebar.text_input('🔗 URL 3')

# Process Button
if st.sidebar.button('🚀 Process URLs'):
    urls = [url for url in (url1, url2, url3) if url.strip()]
    if not urls:
        st.warning("⚠️ Please enter at least one valid URL.")
    else:
        with st.spinner("Processing URLs..."):
            for status in process_urls(urls):
                st.success(status)
        st.balloons()

# Divider
st.markdown("---")

# Question input
st.markdown("### ❓ Ask a Question")
query = st.text_input("Type your question here...", placeholder="e.g., What is the main idea of the article?")

# Display answer
if query:
    try:
        answer, sources = generate_answer(query)
        st.markdown("### ✅ Answer")
        st.success(answer)

        if sources:
            st.markdown("### 🔍 Sources")
            for source in sources.split("\n"):
                st.markdown(f"- {source}")
    except RuntimeError:
        st.error("⚠️ Please process the URLs before asking a question.")
