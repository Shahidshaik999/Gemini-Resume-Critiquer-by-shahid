import streamlit as st
import PyPDF2
import io
import os
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

st.set_page_config(page_title="Gemini Resume Critiquer", page_icon="📃", layout="centered")

st.title("📃 Gemini Resume Critiquer")
st.markdown("Upload your resume and get AI-powered feedback tailored to your target job role using **Google Gemini**!")

# Configure Gemini API
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=GOOGLE_API_KEY)

uploaded_file = st.file_uploader("Upload your resume (PDF or TXT)", type=["pdf", "txt"])
job_role = st.text_input("Enter the job role you're targeting (optional)")

analyze = st.button("Analyze Resume")

# Function to extract text from PDF
def extract_text_from_pdf(pdf_file):
    pdf_reader = PyPDF2.PdfReader(pdf_file)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text() + "\n"
    return text

# Function to extract text from uploaded file
def extract_text_from_file(uploaded_file):
    if uploaded_file.type == "application/pdf":
        return extract_text_from_pdf(io.BytesIO(uploaded_file.read()))
    return uploaded_file.read().decode("utf-8")

if analyze and uploaded_file:
    try:
        # Extract resume content
        file_content = extract_text_from_file(uploaded_file)

        if not file_content.strip():
            st.error("File does not have any content...")
            st.stop()

        # Prompt for Gemini
        prompt = f"""
        You are an expert resume reviewer with years of experience in HR, recruitment, and ATS optimization.

        Please analyze the following resume and provide detailed feedback based on:
        1️⃣ Content clarity and impact  
        2️⃣ Skills presentation  
        3️⃣ Experience relevance and descriptions  
        4️⃣ ATS keyword optimization  
        5️⃣ Suggestions for improvement tailored to {'the role of ' + job_role if job_role else 'general job applications'}  

        Resume Content:
        {file_content}

        Please respond in a clear, structured, and actionable format:
        - **Overall Summary**
        - **Strengths**
        - **Weaknesses**
        - **Specific Recommendations**
        - **ATS Compatibility Score (0–100)**
        """

        # Call Gemini API
        model = genai.GenerativeModel("models/gemini-2.5-flash")
        response = model.generate_content(prompt)

        # Display results
        st.markdown("### 🧠 Resume Analysis Results")
        st.markdown(response.text)

    except Exception as e:
        st.error(f"An error occurred: {str(e)}")
