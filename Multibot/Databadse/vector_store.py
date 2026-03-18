from langchain.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings

embedding = HuggingFaceEmbeddings()# i think here we can specify the model name and version

def create_vector_store(texts):
    vectorstore = FAISS.from_texts(texts, embedding)
    return vectorstore