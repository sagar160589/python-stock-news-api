import requests,os,math

STOCK = 'AAPL'
COMPANY_NAME = 'Apple'
STOCK_API = 'https://www.alphavantage.co/query?'
FUNCTION = 'TIME_SERIES_DAILY_ADJUSTED'
STOCK_API_KEY = os.getenv('stock_api_key')


#Calculate stock close difference between yesterday and day before yesterday
def calculate_stock_close_percentage(stock_data):
    stock_yest = list(stock_data["Time Series (Daily)"].items())[0][1]['4. close']
    stock_day_before = list(stock_data["Time Series (Daily)"].items())[1][1]['4. close']
    return math.ceil(((float(stock_yest) - float(stock_day_before)) / float(stock_yest)) * 100)


class Stock:

    def __init__(self):
        self.stock_name = STOCK,
        self.stock_api = 'https://www.alphavantage.co/query?'
        self.function = FUNCTION
        self.api_key = STOCK_API_KEY,
        self.stock_symbol = None
        self.params = {
            "function": FUNCTION,
            "symbol": STOCK,
            "apikey": STOCK_API_KEY
        }

    #Get stock data from stock api
    def get_stock_data(self):
        stock_api_response = requests.get(self.stock_api, params=self.params)
        stock_api_response.raise_for_status()
        stock_data = stock_api_response.json()
        return calculate_stock_close_percentage(stock_data)

