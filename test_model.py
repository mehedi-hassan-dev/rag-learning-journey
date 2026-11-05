from sentence_transformers import SentenceTransformer

model = SentenceTransformer(
    "/home/mehedi-hassan/models/all-MiniLM-L6-v2"
)

texts = [
    "RAG combines retrieval with generation.",
    "FAISS is used for vector search.",
    "ChromaDB stores embeddings locally."
]

embeddings = model.encode(texts)

print(embeddings.shape)
print("Local model is working.")
