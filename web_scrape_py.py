import requests
from bs4 import BeautifulSoup


class WebScraper:
    def __init__(self, url, headers=None):
        self.url = url

    @staticmethod
    def extract_paragraphs(self, html_content):
        if html_content:
            soup = BeautifulSoup(html_content, 'html.parser')
            paragraph = [p.text for p in soup.find_all('p')]
            return paragraph
        else:
            return []

    def fetch_page(self):
        response = requests.get(self.url)
        if response.status_code == 200:
            return response.text
        else:
            print(f"Failed to fetch the page. Status code: {response.status_code}")
            return None

    def fetch_and_extract_p(self):
        response = requests.get(self.url)
        if response.status_code == 200:
            paragraph = self.extract_paragraphs(self, response.text)
            return " ".join(paragraph)
        else:
            print(f"Failed to fetch the page. Status code: {response.status_code}")
            return None


if __name__ == "__main__":
    # Example use-case
    url = 'https://theathletic.com/5193237/2024/01/10/pete-carroll-not-returning-as-seahawks-coach-will-remain-with-franchise-as-advisor/'

    scraper = WebScraper(url)
    par = scraper.fetch_and_extract_p()
    print(par)
