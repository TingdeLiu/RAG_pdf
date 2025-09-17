# qbot.py      
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain.chains import RetrievalQA
from langchain_google_genai import ChatGoogleGenerativeAI, GoogleGenerativeAIEmbeddings
import os
import gradio as gr


from dotenv import load_dotenv
load_dotenv()

## LLM
def get_llm():
    
    LLM_MODEL = "gemini-2.5-flash-preview-05-20"
    
    google_llm = ChatGoogleGenerativeAI(
        model=LLM_MODEL,
        temperature=0.5,
        max_tokens=256,
    )
    
    return google_llm

## Document loader
def documents_loader(file: str):
    loader = PyPDFLoader(file.name)
    loaded_documents = loader.load()
    return loaded_documents

## Text splitter
def text_splitter(documents):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=100, # size of each chunk
        chunk_overlap=20, # overlap for better context
        length_function=len, # function to measure length
    )
    texts = text_splitter.split_documents(documents)
    return texts

## Embedding model
def google_embedding():
    EMBEDDING_MODEL = "models/text-embedding-004"
    
    embedding_model = GoogleGenerativeAIEmbeddings(model=EMBEDDING_MODEL)
    return embedding_model


## Vector db
def vector_database(chunks):
    embedding_model = google_embedding()
    vectordb = Chroma.from_documents(chunks , embedding_model)
    return vectordb

## Retriever
def retriever(file):
    splits = documents_loader(file)
    chunks = text_splitter(splits)
    vectordb = vector_database(chunks)
    retriever = vectordb.as_retriever()
    return retriever

## QA Chain
def retriever_qa(file, query):
    llm = get_llm()
    retriever_obj = retriever(file)
    qa = RetrievalQA.from_chain_type(llm=llm, 
                                    chain_type="stuff", 
                                    retriever=retriever_obj, 
                                    return_source_documents=False)
    response = qa.invoke(query)
    return response['result']


rag_application = gr.Interface(
    fn=retriever_qa,
    flagging_mode="never",
    inputs=[
        gr.File(label="Upload PDF File", file_count="single", file_types=['.pdf'], type="filepath"),  # Drag and drop file upload
        gr.Textbox(label="Input Query", lines=2, placeholder="Type your question here...")
    ],
    outputs=gr.Textbox(label="Output"),
    title= 'QA Bot',
    description="Upload a PDF document and ask any question. The chatbot will try to answer using the provided document."
)



if __name__ == "__main__":
    # Launch the app
    rag_application.launch(server_name="127.0.0.1", server_port= 7860)
