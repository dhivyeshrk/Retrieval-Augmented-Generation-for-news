# Retrieval-Augmented-Generation-for-news
![img.png](img.png)
A RAG (Retrival Augmented Generation) based fully open source software which provides summaries of related news
articles built using ChromaDB vector database, mixtral-8x7b-instruct-v0.1 LLM (through Replicate AI), New York Times web scraper, dhivyeshrk/bart-large-cnn-samsum Fine-Tuned model for text summarization and sentence-transformers/sentence-t5-base embeddings from HuggingFace.

# System Architecture
## Data Collection 
Data for different categories of news articles were obtained from the following rss-formatted files : 
Technology:  https://rss.nytimes.com/services/xml/rss/nyt/Technology.xml
Sports:  https://rss.nytimes.com/services/xml/rss/nyt/Sports.xml
Science:  https://rss.nytimes.com/services/xml/rss/nyt/Science.xml
Health:  https://rss.nytimes.com/services/xml/rss/nyt/Science.xml

The headlines, descriptions and domains for every news article is vectorized using the sentence-t5-base embeddings and stored in a persistent ChromaDB Client. Links to the respective news articles are also stored in the metadata. In addition, news from each domain is stored in a different ChromaDB collection instance for efficient retrieval. 

## Web Scraping 
Web Scraping has been done using the scraper provided by NY Times API, which only gives ~40-60 words from the news. The wall can be bypassed easily even with BeautifulSoup4 but not quite sure about its legality.

## Data Formatting
For prompt categorization, we have used the mixtral-8x7b-instruct-v0.1 model due to its exceptional capabilities, cloud-based execution on Replicate AI and effortless preventability of hallucination. For text-summarization, we use a fine-tuned version of the bart-large model from HuggingFace originally proposed by Facebook. The model has been trained on cnn_dailymail dataset and further fine-tuned on samsum dataset, achieving 103% improvement in rouge2 benchmark. It is a fairly lightweight model with a size of ~ 1.6 GB.
Links : 
https://huggingface.co/dhivyeshrk/bart-large-cnn-samsum
https://replicate.com/mistralai/mixtral-8x7b-instruct-v0.1

# Usage 
Use your API keys from New York Times API and Replicate AI API and replace them in web_scrape_nyt.py and categorize_prompt.py respectively. 
Then run main.py
