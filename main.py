
import streamlit as st
import os
from agent import ResumeAgent

# Initialize Agent
agent = ResumeAgent()

st.set_page_config(page_title="AI Resume Analyzer", layout="wide")

st.title("🤖 AI Resume Analyzer ")
st.write("Upload your resume and get AI-powered insights!")

# Upload Resume
uploaded_file = st.file_uploader("Upload Resume (PDF/DOCX)", type=["pdf", "docx"])

# Job Description Input
job_description = st.text_area("Paste Job Description")

if st.button("Analyze Resume"):
    if uploaded_file is not None and job_description:


        # Save uploaded file temporarily
        save_dir = r"C:\Users\Dell\Desktop\resume"

# Create folder if not exists
    os.makedirs(save_dir, exist_ok=True)

    file_path = os.path.join(save_dir, uploaded_file.name)

    with open(file_path, "wb") as f:
     f.write(uploaded_file.read())

     st.info("Processing... ⏳")

        # Run Agent
    result = agent.run(file_path, job_description)

    st.success("Analysis Complete ✅")

        # Display Results
    st.subheader("📊 Structured Data")
    st.json(result["structured_data"])

    st.subheader("🤖 AI Analysis")
    st.write(result["analysis"])

    st.subheader("💼 Job Match")
    st.write(result["job_match"])

    st.subheader("📈 Resume Score")
    st.write(result["score"])

    st.subheader("📚 RAG Insights")
    for item in result["rag_context"]:
            st.write(f"- {item}")

    else:
        st.warning("Please upload resume and enter job description")



