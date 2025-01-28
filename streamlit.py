import streamlit as st
import main as main

st.title("Chat with PDFs with Deepseek")

uploaded_file = st.file_uploader(
    "Upload PDF",
    type="pdf",
    accept_multiple_files=False
)

if uploaded_file:
    main.upload_pdf(uploaded_file)
    documents = main.load_pdf(main.pdfs_directory + uploaded_file.name)
    chunked_documents = main.split_text(documents)
    main.vector_index(chunked_documents)

    question = st.chat_input()

    if question:
        st.chat_message("user").write(question)
        related_documents = main.retrieve_docs(question)
        answer = main.answer_question(question, related_documents)
        st.chat_message("assistant").write(answer)