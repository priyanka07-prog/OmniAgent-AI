from database.vector_store import create_vector_store

def rag_bot(question, documents):
    
    vector_store = create_vector_store(documents)
    
    docs = vector_store.similarity_search(question)
    
    return docs[0].page_content
    