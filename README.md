# RAG PDF

An intelligent question-answering system based on Retrieval-Augmented Generation (RAG) technology that allows users to upload PDF documents and ask questions about their content.

## Features

- 📄 **PDF Document Upload**: Support for uploading PDF files as knowledge base
- 🔍 **Intelligent Retrieval**: Vector database-powered similarity search
- 🤖 **AI Question Answering**: Accurate responses powered by Google Gemini model
- 🌐 **Web Interface**: Clean and intuitive Gradio web interface
- ⚡ **Real-time Processing**: Fast document parsing and response generation

## Technology Stack

- **LLM Model**: Google Gemini 2.5 Flash Preview
- **Vector Database**: ChromaDB
- **Document Processing**: PyPDF + LangChain
- **Embedding Model**: Google Text Embedding 004
- **Web Framework**: Gradio
- **Text Splitting**: RecursiveCharacterTextSplitter

## Installation

Ensure you have Python 3.13 or higher installed, then install the project dependencies:

```bash
# Install dependencies using uv (recommended)
uv sync
```

## Configuration

1. Configure your Google API key in the `.env` file:

```bash
GOOGLE_API_KEY="your_google_api_key_here"
```

2. Get your Google API key:
   - Visit [Google AI Studio](https://aistudio.google.com/)
   - Create an API key and replace the placeholder in the `.env` file

## Usage

### Starting the Application

```bash
python qbot.py
```

The application will start at `http://127.0.0.1:7860`

### How to Use

1. **Upload PDF Document**: Drag and drop or select a PDF file in the web interface
2. **Enter Question**: Type your question in the text box
3. **Get Answer**: The system will generate an answer based on the uploaded document content

## Project Structure

```
RAG_pro/
├── qbot.py          # Main application file
├── main.py          # Simple entry point file
├── pyproject.toml   # Project configuration and dependencies
├── .env             # Environment variables configuration
├── data.md          # Sample data file
├── Testdaf.pdf      # Test PDF file
└── README.md        # Project documentation
```

## Core Functionality

### Document Processing Pipeline

1. **Document Loading**: Parse PDF files using PyPDFLoader
2. **Text Splitting**: Split long documents into chunks (chunk_size=100, overlap=20)
3. **Vectorization**: Generate text vectors using Google embedding model
4. **Storage**: Store vectors in ChromaDB vector database

### Question Answering Pipeline

1. **Query Vectorization**: Convert user questions to vectors
2. **Similarity Search**: Retrieve relevant document chunks from vector database
3. **Context Building**: Use retrieved document chunks as context
4. **Answer Generation**: Generate answers using Gemini model based on context

## Customization

You can adjust the following parameters in `qbot.py`:

- **LLM Model**: Modify the `LLM_MODEL` variable
- **Temperature**: Adjust the `temperature` parameter (0-1)
- **Max Tokens**: Modify the `max_tokens` parameter
- **Text Splitting**: Adjust `chunk_size` and `chunk_overlap`
- **Server Configuration**: Modify `server_name` and `server_port`

## Important Notes

- Ensure PDF files are in readable text format (not scanned images)
- Large files may require longer processing time
- Maintain internet connection for Google API calls
- Keep your API key secure and don't commit it to public repositories

## License

This project is released under an open source license.

## Contributing

Issues and Pull Requests are welcome to improve this project.
