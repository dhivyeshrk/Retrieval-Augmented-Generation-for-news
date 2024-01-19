import chromadb
from chromadb.utils import embedding_functions
from relevant_info import XMLParser

def add_embeddings(collection_name, xml_filepath):
    # First Parse and Extract
    xml_parser = XMLParser(xml_filepath)
    xml_parser.parse_xml()
    result = xml_parser.extract_information()

    # Now Add it to the respective collection
    for ind, res in enumerate(result):
        domains = ""
        for domain in res['domains']:
            domains += f"{domain}, "
        collection_name.add(
            documents=f"{res['title']}" + f" Domains : {domains}",
            metadatas=[{'link':res['link']}],
            ids = [f'id{ind}']
        )

if __name__ == "__main__":
    client = chromadb.PersistentClient(path="Retrieval-Augmented-Generation-for-news-Final/ChromaDB_data_populate/DataBase/data")
    sentence_transformer_ef = embedding_functions.SentenceTransformerEmbeddingFunction(model_name="sentence-transformers/sentence-t5-base")

    health_col = client.get_or_create_collection(name="Health", embedding_function=sentence_transformer_ef)
    science_col = client.get_or_create_collection(name="Science", embedding_function=sentence_transformer_ef)
    sports_col = client.get_or_create_collection(name="Sports", embedding_function=sentence_transformer_ef)
    tech_col = client.get_or_create_collection(name="Technology", embedding_function=sentence_transformer_ef)

    path = "Retrieval-Augmented-Generation-for-news-Final/ChromaDB_data_populate/news_xml_files"

    add_embeddings(health_col, path + '/Health.xml')
    add_embeddings(science_col, path + '/Science.xml')
    add_embeddings(sports_col, path + '/Sports.xml')
    add_embeddings(tech_col, path + '/Technology.xml')

    print(health_col.peek())

