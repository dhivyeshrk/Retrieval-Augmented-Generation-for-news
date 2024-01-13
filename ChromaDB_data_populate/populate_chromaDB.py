import chromadb
from InstructorEmbedding import INSTRUCTOR

import chromadb
from chromadb.config import Settings


client = chromadb.Client(Settings(chroma_db_impl="duckdb+parquet",
                                  persist_directory="db/"
                                  ))


# model = INSTRUCTOR('hkunlp/instructor-large')
# sentence = "3D ActionSLAM: wearable person tracking in multi-floor environments"
# instruction = "Represent the Science title:"
# embeddings = model.encode([instruction,sentence])
