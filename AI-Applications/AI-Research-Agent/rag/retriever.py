
from vector_store.vector_store import VectorStore
import numpy as np
import os
from rag.openai_embed import embed_openai
from typing import List, Callable

class Retriever:
    def __init__(self, kernel=None, vector_store_path=None, embed_fn: Callable = None):
        self.kernel = kernel
        path = vector_store_path or os.getenv("VECTOR_STORE_PATH", "rag/store")
        self.store = VectorStore(path=path)
        self.embed_fn = embed_fn or embed_openai

    def add_document(self, text: str):
        vec = self.embed_fn(text)
        self.store.add(vec, text)
        self.store.save()

    def search(self, query: str, k: int = 5) -> List[str]:
        vec = self.embed_fn(query)
        return self.store.search(vec, k=k)
