from dotenv import load_dotenv
import os
import streamlit as st
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

load_dotenv()
API_KEY = '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'

llm = OpenAI(openai_api_key=API_KEY, temperature=0.1)

prompt_template = PromptTemplate(
    input_variables=["ingredients"],
    template="Me de pelo menos um exemplo de receita que podem ser feita com os seguintes ingredientes: {ingredients}",
)

meal_chain = LLMChain(
    llm=llm,
    prompt=prompt_template,
    output_key="meals",  # the output from this chain will be called 'meals'
    verbose=True
)

st.title("Planejando a Refeição")
user_prompt = st.text_input(
    "De uma lista de ingredientes separados por virgula:")

if st.button("Generate") and user_prompt:
    with st.spinner("Generating..."):
        output = meal_chain({'ingredients': user_prompt})
        st.write(output)
