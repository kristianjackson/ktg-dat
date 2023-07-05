# KTG Document Analysis Tool

This Streamlit application uses the power of OpenAI and the Langchain library to provide conversational retrieval from uploaded PDF documents.

## Features

- Upload a PDF document for analysis.
- Query the uploaded document with a text-based question.
- Get a response based on the contents of the uploaded document.

## How it Works

The application uses the Langchain library to load and split the PDF document into chunks, generate embeddings of these chunks using OpenAI's API, and store these embeddings in a Chroma vector database. It then uses a Conversational Retrieval Chain from the Langchain library to answer queries based on the uploaded document.

## Usage

1. Run the Streamlit application.
2. Upload a PDF document you want to query.
3. Enter your question in the input field.
4. Enter your OpenAI API key in the sidebar.
5. Click 'Submit'.
6. The answer to your question, based on the uploaded document, will be displayed.

## Requirements

- Python 3.6 or later
- Streamlit
- Langchain library
- OpenAI API key

## Installation

```bash
pip install streamlit langchain openai
```

**Note:** This application requires an OpenAI API key, which you can get from the [OpenAI platform](https://platform.openai.com/account/api-keys).

## Security

This application requires the use of a private OpenAI API key. Please make sure you do not publicly share this key.

## Disclaimer

This tool does not guarantee 100% accuracy in its responses. Please verify the responses independently if necessary.
