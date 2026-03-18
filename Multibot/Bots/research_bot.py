from tools.web_search import web_search

def research_bot(query):
    
    results = web_search(query)
    return "\n."join(results)
