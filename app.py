import streamlit as st
from pypdf import PdfReader
import os

# -----------------------------
# Page Configuration
# -----------------------------

st.set_page_config(
    page_title="Smart Document Management System",
    page_icon="📚",
    layout="wide"
)

# -----------------------------
# Title
# -----------------------------

st.title("📚 Smart Document Management System")

st.write(
    "Upload, store and manage your documents easily."
)

# -----------------------------
# Upload Document
# -----------------------------

st.header("📤 Upload Document")

uploaded_file = st.file_uploader(
    "Choose a PDF document",
    type=["pdf"]
)

# -----------------------------
# Process Uploaded Document
# -----------------------------

if uploaded_file:

    st.success(
        f"Uploaded: {uploaded_file.name}"
    )

    # Save uploaded file
    file_path = os.path.join(
        "documents",
        uploaded_file.name
    )

    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    st.success("Document saved successfully!")

    # -------------------------
    # Extract PDF Text
    # -------------------------

    reader = PdfReader(uploaded_file)

    text = ""

    for page in reader.pages:

        page_text = page.extract_text()

        if page_text:
            text += page_text + "\n"

    # -------------------------
    # Display Text
    # -------------------------

    st.header("📄 Extracted Document Text")

    st.text_area(
        "Document Content",
        text,
        height=400
    )