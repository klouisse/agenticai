import os
import streamlit as st
from langchain_groq import ChatGroq

#this class is responsible for initializing the GROQ LLM based on the user input from the UI.
#  It retrieves the GROQ API key and the selected GROQ model from the user controls input, 
# and then initializes the ChatGroq LLM with those parameters.
#  If there is an error during this process, it raises a ValueError with the appropriate error message.
class GroqLLM:
    def __init__(self,user_contols_input):
        self.user_controls_input=user_contols_input

    def get_llm_model(self):
        try:
            groq_api_key=self.user_controls_input["GROQ_API_KEY"]
            selected_groq_model=self.user_controls_input["selected_groq_model"]
            if groq_api_key=='' and os.environ["GROQ_API_KEY"] =='':
                st.error("Please Enter the Groq API KEY")

            llm=ChatGroq(api_key=groq_api_key,model=selected_groq_model)

        except Exception as e:
            raise ValueError(f"Error Ocuured With Exception : {e}")
        return llm