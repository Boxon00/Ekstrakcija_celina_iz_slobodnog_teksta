from sentence_transformers import SentenceTransformer

def create_embeddings(sentences):
    model = SentenceTransformer('all-MiniLM-L6-v2')
    embeddings = model.encode(sentences, show_progress_bar=True)
    return embeddings
