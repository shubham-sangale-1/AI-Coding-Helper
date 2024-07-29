import os
import google.generativeai as genai
import streamlit as st
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get the API key from environment variables
key = os.getenv("GOOGLE_API_KEY")

if not key:
    raise ValueError("API key not found in environment variables")

genai.configure(api_key=key)

class GeminiAIHelper:
    def __init__(self, model_name='gemini-1.5-flash'):
        self.model = genai.GenerativeModel(model_name)

    def generate_response(self, prompt):
        response = self.model.generate_content(prompt)
        return response.text

    def suggest_code(self, code):
        prompt = f"Suggest the next lines of code for the following code snippet:\n{code}"
        return self.generate_response(prompt)

    def help_debug(self, code):
        prompt = f"Find and fix errors in the following code snippet and explain the issues:\n{code}"
        return self.generate_response(prompt)

    def give_tips(self, code):
        prompt = f"Provide tips to improve the following code snippet:\n{code}"
        return self.generate_response(prompt)

    def complete_code(self, code):
        prompt = f"Complete the following incomplete code snippet:\n{code}"
        return self.generate_response(prompt)

def main():
    ai_helper = GeminiAIHelper()
    st.title("AI Coding Helper")

    st.write("Enter your code below to receive suggestions, debugging help, improvement tips, and completion.")

    code_input = st.text_area("Your Code:", height=300)

    if len(code_input) > 10:
        st.write("Click the buttons below to get different types of assistance:")
        col1, col2, col3, col4 = st.columns([1, 1, 1, 1])

        with col1:
            if st.button("Suggest Code"):
                try:
                    suggestion = ai_helper.suggest_code(code_input)
                    st.session_state.suggestion = suggestion
                except Exception as e:
                    st.error(f"An error occurred: {e}")

        with col2:
            if st.button("Help Debug"):
                try:
                    debugging_help = ai_helper.help_debug(code_input)
                    st.session_state.debugging_help = debugging_help
                except Exception as e:
                    st.error(f"An error occurred: {e}")

        with col3:
            if st.button("Give Tips"):
                try:
                    tips = ai_helper.give_tips(code_input)
                    st.session_state.tips = tips
                except Exception as e:
                    st.error(f"An error occurred: {e}")

        with col4:
            if st.button("Complete Code"):
                try:
                    completion = ai_helper.complete_code(code_input)
                    st.session_state.completion = completion
                except Exception as e:
                    st.error(f"An error occurred: {e}")

        if 'suggestion' in st.session_state:
            st.text_area("Code Suggestions:", st.session_state.suggestion, height=300)

        if 'debugging_help' in st.session_state:
            st.text_area("Debugging Help:", st.session_state.debugging_help, height=300)

        if 'tips' in st.session_state:
            st.text_area("Improvement Tips:", st.session_state.tips, height=300)

        if 'completion' in st.session_state:
            st.text_area("Completed Code:", st.session_state.completion, height=300)
    else:
        st.warning("Please enter code with more than 10 characters.")

    st.markdown("<h5 style='color: green;'>Developer: Shubham Sangale</h5><br><a href='https://www.linkedin.com/in/shubham-sangale-81568722a?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app'><h6 style='color: blue;'>LinkedIn</h6></a>", unsafe_allow_html=True)
    st.markdown('<div class="footer">© 2024 Information Generator. All rights reserved.</div>', unsafe_allow_html=True)

if __name__ == "__main__":
    main()
