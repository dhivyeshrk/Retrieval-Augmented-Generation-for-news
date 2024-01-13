import requests
from bs4 import BeautifulSoup


class WebScraper:
    def __init__(self, url, headers=None):
        self.url = url
        # Mimic a browser to bypass the wall
        self.headers = headers or {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
        }

    def extract_paragraphs(self, html_content):
        if html_content:
            soup = BeautifulSoup(html_content, 'html.parser')
            paragraph = [p.text for p in soup.find_all('p')]
            return paragraph
        else:
            return []

    def fetch_page(self):
        response = requests.get(self.url, headers=self.headers)
        if response.status_code == 200:
            return response.text
        else:
            print(f"Failed to fetch the page. Status code: {response.status_code}")
            return None

    def fetch_and_extract_p(self):
        response = requests.get(self.url, headers=self.headers)
        if response.status_code == 200:
            par =  self.extract_paragraphs(response.text)
            return " ".join(par)
        else:
            print(f"Failed to fetch the page. Status code: {response.status_code}")
            return None


if __name__ == "__main__":
    # Example use-case
    url = 'https://www.nytimes.com/2024/01/11/health/gaza-israel-hunger-starvation.html'

    scraper = WebScraper(url)
    par = scraper.fetch_and_extract_p()
    print(par)