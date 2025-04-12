import streamlit as st
import fitz  # PyMuPDF for PDF text extraction
import openai
import os

# Set your OpenAI API key
openai.api_key = "YOUR_OPENAI_API_KEY"  # <-- Replace with your actual key or use environment variable

# Function to extract text from the uploaded resume (PDF)
def extract_text_from_pdf(uploaded_file):
    # Read uploaded file properly
    file_bytes = uploaded_file.read()
    doc = fitz.open(stream=file_bytes, filetype="pdf")
    full_text = ""
    for page in doc:
        full_text += page.get_text()
    doc.close()
    return full_text

# Function to process resume using OpenAI's GPT-3/4
def process_resume_with_ai(resume_text):
    prompt = f"Extract the following details from the resume: Name, Skills, Education, and Experience.\n\nResume Text:\n{resume_text}"
    
    response = openai.Completion.create(
        engine="text-davinci-003",  # or use "gpt-4" if you have access
        prompt=prompt,
        max_tokens=500,
        temperature=0.5
    )
    
    ai_output = response.choices[0].text.strip()
    return ai_output

# Streamlit App
def main():
    st.title("✨ TalentTrek - Resume Screening ✨")
    st.write("Upload your resume as a PDF and let AI screen it for you!")

    uploaded_file = st.file_uploader("Upload your Resume (PDF)", type=["pdf"])
    
    if uploaded_file is not None:
        st.subheader("Uploaded Resume Text")

        # Extract text from the uploaded resume
        resume_text = extract_text_from_pdf(uploaded_file)
        
        # Display extracted text (optional)
        st.text_area("Resume Text", resume_text, height=300)
        
        # Button to process resume
        if st.button("Screen Resume"):
            with st.spinner("Processing with AI..."):
                ai_output = process_resume_with_ai(resume_text)
                st.subheader("🔎 Screened Resume Details")
                st.text_area("Resume Details", ai_output, height=300)

if __name__ == "__main__":
    main()
qax
