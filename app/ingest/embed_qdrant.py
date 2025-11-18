from qdrant_client import QdrantClient
from app.utils.settings import settings
from openai import OpenAI
from langchain_qdrant import QdrantVectorStore
from langchain.embeddings import HuggingFaceEmbeddings
import os

class EmbeddingSelfQuery:
    def __init__(self) -> None:
        self.llm = OpenAI(
            api_key=settings.GROQ_API("GROQ_API_KEY"),
            base_url="https://api.groq.com/openai/v1",
            temperature=0
        )
        self.client = QdrantClient(
            host=settings.QDRANT_HOST,
            port=settings.QDRANT_PORT,
            timeout=120,
        )
        self.model_embedding = HuggingFaceEmbeddings(
            model_name="sentence-transformers/all-MiniLM-L6-v2"
        )

    def get_qdrant_vector_store(self, collection_name: str) -> QdrantVectorStore:
        return QdrantVectorStore(
            client=self.client,
            collection_name=collection_name,
            embedding=self.model_embedding,
            sparse_vector_name="text-sparse",
            vector_name="text-dense",
        )
