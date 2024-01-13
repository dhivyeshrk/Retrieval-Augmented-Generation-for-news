import chromadb
from chromadb.utils import embedding_functions


client = chromadb.PersistentClient(path="ChromaDB_data_populate/DataBase/data")
sentence_transformer_ef = embedding_functions.SentenceTransformerEmbeddingFunction(model_name="sentence-transformers/sentence-t5-base")

# Get collections for each news type
health_col = client.get_collection(name="Health", embedding_function=sentence_transformer_ef)
science_col = client.get_collection(name="Science", embedding_function=sentence_transformer_ef)
sports_col = client.get_collection(name="Sports", embedding_function=sentence_transformer_ef)
tech_col = client.get_collection(name="Technology", embedding_function=sentence_transformer_ef)

result = health_col.query(
    query_texts=['starvation'],
    n_results=2
)

links = []
for i in result['metadatas'][0]:
    links.append(i['link'])
