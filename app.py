import streamlit as st
import fitz  # PyMuPDF for PDF text extraction
import openai
import os

# Set your OpenAI API key here
openai.api_key = "YOUR_OPENAI_API_KEY"

# Function to extract text from the uploaded resume (PDF)
def extract_text_from_pdf(pdf_file):
    doc = fitz.open(pdf_file)
    full_text = ""
    for page in doc:
        full_text += page.get_text()
    return full_text

# Function to process resume using OpenAI's GPT-3/4
def process_resume_with_ai(resume_text):
    prompt = f"Please extract the following details from the resume: Name, Skills, Education, and Experience.\n\nResume Text: {resume_text}"
    
    # Send the prompt to the OpenAI model
    response = openai.Completion.create(
        engine="text-davinci-003",  # You can also use "gpt-4" here
        prompt=prompt,
        max_tokens=500
    )
    
    # Extract relevant information from the AI response
    ai_output = response.choices[0].text.strip()
    return ai_output

# Streamlit App UI
def main():
    st.title("TalentTrek - Resume Screening")
    
    # Upload the resume (PDF file)
    uploaded_file = st.file_uploader("Upload your Resume (PDF)", type=["pdf"])
    
    if uploaded_file is not None:
        st.subheader("Uploaded Resume Text")
        
        # Extract text from the uploaded resume
        resume_text = extract_text_from_pdf(uploaded_file)
        
        # Show extracted text for verification (can be commented out later)
        st.text_area("Resume Text", resume_text, height=300)
        
        # Process resume with AI (OpenAI GPT-3 or GPT-4)
        if st.button("Screen Resume"):
            with st.spinner("Processing..."):
                ai_output = process_resume_with_ai(resume_text)
                st.subheader("Processed Resume Details:")
                st.text_area("Resume Details", ai_output, height=300)

if __name__ == "__main__":
    main()
import streamlit as st
import fitz  # PyMuPDF for PDF text extraction
import openai
import os

# Set your OpenAI API key here
openai.api_key = "YOUR_OPENAI_API_KEY"

# Function to extract text from the uploaded resume (PDF)
def extract_text_from_pdf(pdf_file):
    doc = fitz.open(pdf_file)
    full_text = ""
    for page in doc:
        full_text += page.get_text()
    return full_text

# Function to process resume using OpenAI's GPT-3/4
def process_resume_with_ai(resume_text):
    prompt = f"Please extract the following details from the resume: Name, Skills, Education, and Experience.\n\nResume Text: {resume_text}"
    
    # Send the prompt to the OpenAI model
    response = openai.Completion.create(
        engine="text-davinci-003",  # You can also use "gpt-4" here
        prompt=prompt,
        max_tokens=500
    )
    
    # Extract relevant information from the AI response
    ai_output = response.choices[0].text.strip()
    return ai_output

# Streamlit App UI
def main():
    st.title("TalentTrek - Resume Screening")
    
    # Upload the resume (PDF file)
    uploaded_file = st.file_uploader("Upload your Resume (PDF)", type=["pdf"])
    
    if uploaded_file is not None:
        st.subheader("Uploaded Resume Text")
        
        # Extract text from the uploaded resume
        resume_text = extract_text_from_pdf(uploaded_file)
        
        # Show extracted text for verification (can be commented out later)
        st.text_area("Resume Text", resume_text, height=300)
        
        # Process resume with AI (OpenAI GPT-3 or GPT-4)
        if st.button("Screen Resume"):
            with st.spinner("Processing..."):
                ai_output = process_resume_with_ai(resume_text)
                st.subheader("Processed Resume Details:")
                st.text_area("Resume Details", ai_output, height=300)

if __name__ == "__main__":
    main()
