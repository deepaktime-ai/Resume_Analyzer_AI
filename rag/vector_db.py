from sentence_transformers import SentenceTransformer
import faiss
import numpy as np


class VectorDB:

    def __init__(self):
        self.model = SentenceTransformer('all-MiniLM-L6-v2')
        self.texts = []
        self.index = None

    def add_texts(self, texts):
        self.texts.extend(texts)

        embeddings = self.model.encode(texts)
        embeddings = np.array(embeddings).astype("float32")

        if self.index is None:
            dim = embeddings.shape[1]
            self.index = faiss.IndexFlatL2(dim)

        self.index.add(embeddings)

    def search(self, query, k=3):
        query_embedding = self.model.encode([query])
        query_embedding = np.array(query_embedding).astype("float32")

        distances, indices = self.index.search(query_embedding, k)

        results = [self.texts[i] for i in indices[0]]
        return results