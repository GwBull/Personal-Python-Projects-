import requests

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"


STOCK_API_KEY = "8SZNC5VBJ3O12SY9"

stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": STOCK_API_KEY,
}
## creates a dictionary called stock_params that contains the parameters needed to make a request to the Alpha Vantage API for daily stock data. 
##The parameters include the function (TIME_SERIES_DAILY), the stock symbol (TSLA), and the API key (STOCK_API_KEY).
## when we send a GET request to the Alpha Vantage API endpoint for daily stock data, we pass this dictionary as the params argument to the requests.get() method. 
##This allows us to retrieve the daily stock data for the specified stock symbol (TSLA) using our API key.

api_response = requests.get(STOCK_ENDPOINT, params=stock_params)


## uses the requests library to make a GET request to the Alpha Vantage API endpoint for daily stock data. The parameters for the request include the function (TIME_SERIES_DAILY), the stock symbol (TSLA), and the API key. The response from the API is stored in the variable api_response.
## these are alpha vantage api parameters that are used to retrieve daily stock data for a specific stock symbol (in this case, TSLA) using the Alpha Vantage API. The parameters include the function (TIME_SERIES_DAILY), the stock symbol (TSLA), and the API key (STOCK_API_KEY). These parameters are passed as a dictionary to the requests.get() method to make a GET request to the Alpha Vantage API endpoint for daily stock data.

data = api_response.json()["Time Series (Daily)"]

data_list = [value for (key, value) in data.items()]

# turns the dictionary into a list so we can get days by POSITION instead of by date
#   data.items()   gives each (date, prices) pair
# the dictionary is built when we say api.response.json()["Time Series (Daily)"], which returns a dictionary where each key is a date and each value is another dictionary containing the stock prices for that date.
# that dictionary is called data, and it contains the daily stock data for TSLA. The items() method is called on the data dictionary to get a list of (key, value) pairs, where each key is a date and each value is another dictionary containing the stock prices for that date.
# time series daily is a dicitonary that returned by the api key where each date is a key 
# this is returned but not explicitly printed in the code, but it is used to create the data_list variable, which is a list of dictionaries containing the stock prices for each date. The list comprehension iterates over each (key, value) pair in the data dictionary and extracts only the value (the dictionary containing the stock prices) to create a new list called data_list.
#   (key, value)   key = the date, value = that day's prices
#   value          keep only the prices and drop the date
#   [ ]            collect them into a new list
# the API sends the newest day first and only includes days the market was open,
# so data_list[0] is always the newest trading day and data_list[1] is the one before
# (weekends and holidays are skipped automatically)

print(data_list[0])  

if difference > 0:
    print (f"TSLA: 🔺{differnce}%")
else:
    print (f"TSLA: 🔻{differnce}%")

## prints the daily stock data for the date "2026-11-17" from the data dictionary. 
## The data dictionary contains the daily stock data for TSLA, and the key "2026-11-17" corresponds to the specific date for which we want to retrieve the stock data.


#TODO 2. - Get the day before yesterday's closing stock price

#TODO 3. - Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20. Hint: https://www.w3schools.com/python/ref_func_abs.asp

#TODO 4. - Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.

#TODO 5. - If TODO4 percentage is greater than 5 then print("Get News").

    ## STEP 2: https://newsapi.org/ 
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

#TODO 6. - Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.

#TODO 7. - Use Python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation

    ## STEP 3: Use twilio.com/docs/sms/quickstart/python
    #to send a separate message with each article's title and description to your phone number. 

#TODO 8. - Create a new list of the first 3 article's headline and description using list comprehension.

#TODO 9. - Send each article as a separate message via Twilio. 



#Optional TODO: Format the message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""


