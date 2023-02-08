from stock import Stock
from twilio_message import Messenger
from news import News

stock = Stock()
messenger = Messenger()
news = News()

stock_difference = stock.get_stock_data()
if stock_difference > 0:
    stock.stock_symbol = "🔺"
else:
    stock.stock_symbol = "🔻"
current_news = news.get_news()
messenger.send_sms(stock.stock_name,stock.stock_symbol,stock_difference,
                   current_news['articles'][0]['title'],
                   current_news['articles'][0]['description'])

