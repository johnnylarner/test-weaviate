import weaviate
from dataclasses import dataclass


@dataclass
class Config:
    ENDPOINT: str = "http://localhost:8080"

    def get_client(self) -> weaviate.Client:
        return weaviate.Client(self.ENDPOINT)
