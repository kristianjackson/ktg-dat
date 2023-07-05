import streamlit as st

from langchain.llms import OpenAI
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from langchain.chains import ConversationalRetrievalChain
from langchain.document_loaders import PyPDFLoader

import os
import tempfile

def generate_response(uploaded_file, openai_api_key, query_text, chat_history):
    # Load document if file is uploaded
    if uploaded_file is not None:
        # Create a temporary file and write the uploaded file's bytes to it
        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as temp_file:
            temp_file.write(uploaded_file.getvalue())
            temp_path = temp_file.name
        loader = PyPDFLoader(temp_path)
        texts = loader.load_and_split()
        embeddings = OpenAIEmbeddings(openai_api_key=openai_api_key)
        db = Chroma.from_documents(texts, embeddings)
        qa = ConversationalRetrievalChain.from_llm(OpenAI(temperature=0), db.as_retriever())
        
        result = qa({"question": query_text, "chat_history": chat_history})

        # Clean up the temporary file
        os.unlink(temp_path)

        return result["answer"]



# Page title
st.set_page_config(page_title='KTG DAT')
st.title('KTG Document Analysis Tool')
st.subheader('DHS Edition')
st.write('Last Updated: 07/05/2023')

# File upload
uploaded_file = st.file_uploader('Upload an article', type='pdf')
# Query text
query_text = st.text_input('Enter your question:', placeholder = 'Provide a summary of the information in less than 500 words', disabled=not uploaded_file)

# Form input and query
result = []
with st.form('myform', clear_on_submit=True):
    openai_api_key = st.sidebar.text_input('OpenAI API Key', type='password', disabled=not (uploaded_file and query_text), value=os.environ.get("OPENAI_API_KEY"), help="https://platform.openai.com/account/api-keys")
    submitted = st.form_submit_button('Submit', disabled=not(uploaded_file and query_text))
    if submitted and openai_api_key.startswith('sk-'):
        with st.spinner('Calculating...'):
            response = generate_response(uploaded_file, openai_api_key, query_text, result)
            result.append(response)
            del openai_api_key

if len(result):
    st.info(response)