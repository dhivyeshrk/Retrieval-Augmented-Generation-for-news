import requests as req

class NYTimesAPI:
    def __init__(self):
        self.api_key = 'COStbacR9mDSMpaeYcrvzD3yj5xql6V3'
        self.base_url = 'https://api.nytimes.com/svc/search/v2/articlesearch.json'

    def get_response(self, keyword):
        # url = self.preprocess(self, keyword)
        url = f'{self.base_url}?q={keyword}&api-key={self.api_key}'
        response = req.get(url).json()
        if 'response' in response and 'docs' in response['response']:
            docs = response['response']['docs']
            abstract = docs[0].get('abstract', '')
            snippet = docs[0].get('snippet', '')
            lead_paragraph = docs[0].get('lead_paragraph', '')
            result = abstract + ' ' + snippet + ' ' + lead_paragraph
            return result
        return None

    @staticmethod
    def preprocess(self, original_url):
        # Extract text after the 6th slash
        parts = original_url.split('/')
        if len(parts) > 6:
            processed_text = '/' + '/'.join(parts[6:])
            return processed_text
        return None


if __name__ == "__main__":
    # Instantiate the NYTimesAPI class
    nytimes_api = NYTimesAPI()

    # Specify the keyword for the article search
    keyword = 'https://www.nytimes.com/2024/01/12/business/arena-bioworks-scientists-harvard-mit.html'

    # Get and print the concatenated information from the response
    concatenated_info = nytimes_api.get_response(keyword)
    if concatenated_info:
        print(concatenated_info)
    else:
        print("No response or invalid response format.")
