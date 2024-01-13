import sys
from categorize_prompt import ReplicateAPI
from web_scrape_nyt import NYTimesAPI
from get_summary import TextSummarizationPipeline
from chromadb.utils import embedding_functions
import chromadb

def get_linksDB(collection_name, user_prompt):
    client = chromadb.PersistentClient(path="ChromaDB_data_populate/DataBase/data")
    sentence_transformer_ef = embedding_functions.SentenceTransformerEmbeddingFunction(model_name="sentence-transformers/sentence-t5-base")
    collection_name = collection_name.capitalize()
    # Get collections for each news type
    db_collection = client.get_collection(name=f"{collection_name}", embedding_function=sentence_transformer_ef)

    result = db_collection.query(
        query_texts=[user_prompt],
        n_results=2
    )
    links = []
    for i in result['metadatas'][0]:
        links.append(i['link'])

    return links


def categorize(prompt : str):
    api = ReplicateAPI(model_name='mistralai/mixtral-8x7b-instruct-v0.1')
    output = api.run_model(prompt)
    output = [element.lower().strip() for element in output]
    categories = ['technology', 'science', 'health', 'sports']
    relevant_category = next((element for element in output if element in categories), None)
    if relevant_category:
        return relevant_category
    else:
        return None


if __name__ == '__main__':

    user_prompt = input("Please enter keywords to find related news :   ")

    # categorize the prompt
    prompt_category = categorize(user_prompt)
    print(f"Your prompt was categorized under {prompt_category}")

    # Highly unlikely case
    if prompt_category is None:
        print("Exiting program because prompt category is None.")
        sys.exit()

    outputs = []
    links = get_linksDB(prompt_category, user_prompt)
    scraper = NYTimesAPI()
    summarizer = TextSummarizationPipeline()
    for link in links:
        info = scraper.get_response(link)
        outputs.append(summarizer.generate_summary(info))

    print("Here are AI generated summaries of some related news articles : ")
    for out in outputs:
        print(out[0]['generated_text'])
        print("-----------------------")

















# Obtain news description from user
# categorize the prompt
# perform similarity search on the database
# get the url
# web scrape
# get_summary