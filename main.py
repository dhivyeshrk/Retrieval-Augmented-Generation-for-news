import sys
from categorize_prompt import ReplicateAPI
from web_scrape_nyt import NYTimesAPI
from web_scrape_py import WebScraper
from get_summary import TextSummarizationPipeline
from chromadb.utils import embedding_functions
import chromadb


def get_linksDB(collection_name, prompt) -> list:
    """
    Fetches related news document links from ChromaDB after performing a semantic search.
    :param collection_name: Name of the related collection
    :param prompt: User prompt to perform semantic search with chromadb
    :return:
    """
    client = chromadb.PersistentClient(path="Retrieval-Augmented-Generation-for-news/ChromaDB_data_populate/DataBase/data")
    sentence_transformer_ef = embedding_functions.SentenceTransformerEmbeddingFunction(model_name="sentence-transformers/sentence-t5-base")
    collection_name = collection_name.capitalize()
    # Get collections for each news type (collection corresponds to table)
    db_collection = client.get_collection(name=f"{collection_name}", embedding_function=sentence_transformer_ef)

    result = db_collection.query(
        query_texts=[prompt],
        n_results=2
    )
    related_links = []
    for i in result['metadatas'][0]:
        related_links.append(i['link'])

    return related_links


def categorize(prompt: str, model: str) -> str:
    """
    Categorizes the prompt using specified LLM from ReplicateAI API
    :param model: Name of LLM
    :param prompt: user_prompt
    :return: categorized category
    """
    api = ReplicateAPI(model_name=model)
    output = api.run_model(prompt)
    output = [element.lower().strip() for element in output]
    categories = ['technology', 'science', 'health', 'sports']
    relevant_category = next((element for element in output if element in categories), None)
    if relevant_category:
        return relevant_category
    else:
        return ""


def get_news(url: str) -> list:
    if 'www.nytimes.com' in url:
        scraper = NYTimesAPI()
        news = scraper.get_response(url)
        return news
    else:
        scraper = WebScraper(url)
        par = scraper.fetch_and_extract_p()
        return par


if __name__ == '__main__':

    user_prompt = input("Please enter keywords to find related news :   ")

    # categorize the prompt
    model_name = 'mistralai/mixtral-8x7b-instruct-v0.1'
    prompt_category = categorize(user_prompt, model_name)
    print(f"Your prompt was categorized under {prompt_category}")

    # Highly unlikely case
    if prompt_category is None:
        print("Exiting program because prompt category is None.")
        sys.exit()

    outputs = []
    # Get the links
    links = get_linksDB(prompt_category, user_prompt)
    # scraper = NYTimesAPI()
    # Summarize the Text
    summarizer = TextSummarizationPipeline()
    for link in links:
        # info = scraper.get_response(link)
        info = get_news(link)
        outputs.append(summarizer.generate_summary(info))

    # Print the outputs
    print("Here are AI generated summaries of some related news articles : ")
    for out in outputs:
        print(out[0]['generated_text'])
        print("-----------------------")
