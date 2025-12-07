import faiss
import os
import pickle
import numpy as np

class VectorStore:
    def __init__(self, path="rag/store", dim=None):
        self.path = path
        self.dim = dim
        os.makedirs(path, exist_ok=True)
        self.index_file = os.path.join(path, "faiss_index.idx")
        self.data_file = os.path.join(path, "faiss_data.pkl")

        if os.path.exists(self.index_file) and os.path.exists(self.data_file):
            self.index = faiss.read_index(self.index_file)
            with open(self.data_file, "rb") as f:
                self.texts = pickle.load(f)
            self.dim = self.index.d
        else:
            self.index = None  # will initialize after first vector
            self.texts = []

    def add(self, vector, text):
        vector = np.array(vector, dtype=np.float32).reshape(1, -1)
        if self.index is None:
            # Initialize FAISS index with the dimension of the first vector
            self.dim = vector.shape[1]
            self.index = faiss.IndexFlatL2(self.dim)
        self.index.add(vector)
        self.texts.append(text)

    def save(self):
        if self.index is not None:
            faiss.write_index(self.index, self.index_file)
        with open(self.data_file, "wb") as f:
            pickle.dump(self.texts, f)

    def search(self, vector, k=5):
        vector = np.array(vector, dtype=np.float32).reshape(1, -1)
        if self.index is None:
            return []
        D, I = self.index.search(vector, k)
        results = []
        for i in I[0]:
            if i < len(self.texts):
                results.append(self.texts[i])
        return results
