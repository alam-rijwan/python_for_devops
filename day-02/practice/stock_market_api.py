import requests
API_KEY = " X2QW9CZABOPOTA3E"  #Step 1: Get API KEY
api_url = "https://www.alphavantage.co/" # Step 2: Get API URL (FindBase URL)

#symbol = "IBM"






def get_stock_data(symbol):

    query = f"query?function=TIME_SERIES_DAILY&symbol={symbol}&apikey={API_KEY}" 


    response = requests.get(url=api_url + query) # Step 5: Make the API request using the full URL
    
    print(response.json())
symbol = input("Please enter the stock symbol ex: IBM, AAPL, MSFT: ")
get_stock_data(symbol)




