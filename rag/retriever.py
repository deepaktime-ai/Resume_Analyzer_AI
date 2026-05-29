from rag.vector_db import VectorDB


class Retriever:

    def __init__(self):
        self.db = VectorDB()

    def load_data(self):
        # Example knowledge base
        texts = [
            "Python is important for machine learning jobs",
            "Cloud computing is required in modern software roles",
            "Data structures and algorithms are critical for interviews",
            "Projects improve resume strength significantly",
            "Communication skills are important in all jobs"
        ]

        self.db.add_texts(texts)

    def get_context(self, query):
        return self.db.search(query)



if __name__ == "__main__":
    retriever = Retriever()
    retriever.load_data()

    query = "What skills are missing for software jobs?"

    results = retriever.get_context(query)

    print("\n🔍 Retrieved Context:\n")
    for r in results:
        print("-", r)

