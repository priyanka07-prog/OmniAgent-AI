from database.vectore_store import create_vector_store

def rag_bot(question, documents):
    
    vectorestore = create_vector_store(documents)
    
    docs = vectorestore.similarity_search(question)
    
    return docs[0].page_content
    