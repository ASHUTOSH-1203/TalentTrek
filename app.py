import streamlit as st
import fitz  # PyMuPDF for PDF text extraction
import openai
import os

# Set your OpenAI API key
openai.api_key = "YOUR_OPENAI_API_KEY"

# Function to extract text from the uploaded resume (PDF)
def extract_text_from_pdf(pdf_file):
    pdf_bytes = pdf_file.read()  # <-- FIXED
    doc = fitz.open(stream=pdf_bytes, filetype="pdf")  # <-- FIXED
    full_text = ""
    for page in doc:
        full_text += page.get_text()
    return full_text

# Function to process resume using OpenAI's GPT
def process_resume_with_ai(resume_text):
    prompt = f"Please extract the following details from the resume: Name, Skills, Education, and Experience.\n\nResume Text: {resume_text}"
    
    response = openai.Completion.create(
        engine="text-davinci-003",  # Or "gpt-4" if available
        prompt=prompt,
        max_tokens=500
    )
    
    ai_output = response.choices[0].text.strip()
    return ai_output

# Streamlit App UI
def main():
    st.title("TalentTrek - Resume Screening")
    
    uploaded_file = st.file_uploader("Upload your Resume (PDF)", type=["pdf"])
    
    if uploaded_file is not None:
        st.subheader("Uploaded Resume Text")
        
        # Extract text from the uploaded resume
        resume_text = extract_text_from_pdf(uploaded_file)
        
        st.text_area("Resume Text", resume_text, height=300)
        
        if st.button("Screen Resume"):
            with st.spinner("Processing..."):
                ai_output = process_resume_with_ai(resume_text)
                st.subheader("Processed Resume Details:")
                st.text_area("Resume Details", ai_output, height=300)

if __name__ == "__main__":
    main()
