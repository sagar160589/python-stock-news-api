# python-stock-news-api

This project is to get stock information of yesterday's and day before yesterday's about a particular company and calulate the stock difference between the closing of both days. It then sends SMS via Twilio API about the stock difference and then the latest stock news of the company.

API & sites used -
1. To get Stock information - https://www.alphavantage.co
2. To get latest news - https://newsapi.org
3. To send SMS - https://www.twilio.com

Note - All above APIs and twilio SMS require authentication & authorization which is done using API Keys. Official documentation available on each of the above websites in order to generate the Free API keys/AccountId/Twilio sender phone number & verification.
API Keys should be stored as enviornmental variables. To run on local, these configs can be stored inside Run -> Edit configuration -> Enviornmental variables.
