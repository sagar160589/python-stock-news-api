import os, requests, datetime as dt


NEWS_API = "https://newsapi.org/v2/everything?"
NEWS_API_KEY = os.getenv("news_api_key")
NEWS_SORT_BY = 'popularity '
COMPANY_NAME = "Apple"


class News:
    def __init__(self):
        self.news_api = NEWS_API,
        self.api_key = NEWS_API_KEY,
        self.news_sort = NEWS_SORT_BY,
        self.params = {
            "q": COMPANY_NAME,
            "from": dt.datetime.now().date(),
            "sortBy": NEWS_SORT_BY,
            "apiKey": NEWS_API_KEY
        }

    #Get Stock news
    def get_news(self):
        news_api_response = requests.get(NEWS_API, params=self.params)
        news_api_response.raise_for_status()
        return news_api_response.json()
