import os
import tempfile

import dotenv
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders.sitemap import SitemapLoader
from langchain_community.vectorstores import SKLearnVectorStore
from langchain_huggingface import HuggingFaceEmbeddings

dotenv.load_dotenv()

RAG_PROMPT = """You are an assistant for writing cold emails to professors for research opportunities. You have
information about all professors in the university. You are supposed to find professors with aligned interests and/ or previous activities.
If you don't know who to suggest, just say that you don't know. Don't write if you can't align the previous activities
with professors' interests.

Context: {context} 
Previous activities: {prev_activities}
Interest: {interests}
Answer:"""

def get_vector_db_retriever():
    persist_path = os.path.join(tempfile.gettempdir(), "union.parquet")
    embd = HuggingFaceEmbeddings(
        model_name="all-MiniLM-l6-v2",
        model_kwargs={'device': 'mps'},
        encode_kwargs={'normalize_embeddings': False}
    )

    # If vector store exists, then load it
    if os.path.exists(persist_path):
        vectorstore = SKLearnVectorStore(
            embedding=embd,
            persist_path=persist_path,
            serializer="parquet"
        )
        return vectorstore.as_retriever(lambda_mult=0)
    faculty_patterns = [
        "https://snu.edu.in/faculty/.*"
    ]

    # Otherwise, index LangSmith documents and create new vector store
    ls_docs_sitemap_loader = SitemapLoader(web_path="https://snu.edu.in/sitemap.seomaestro.xml", continue_on_failure=True, filter_urls=faculty_patterns)

    ls_docs = ls_docs_sitemap_loader.load()

    text_splitter = RecursiveCharacterTextSplitter.from_tiktoken_encoder(
        chunk_size=500, chunk_overlap=0
    )
    doc_splits = text_splitter.split_documents(ls_docs)

    vectorstore = SKLearnVectorStore.from_documents(
        documents=doc_splits,
        embedding=embd,
        persist_path=persist_path,
        serializer="parquet"
    )
    vectorstore.persist()
    return vectorstore.as_retriever(lambda_mult=0)
