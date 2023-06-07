""" 
    Title: Problemset_4 - Bitcoin Price Index

    Author: Emely Benke
    
    Created: 2023-06-05
    
    Version: 0.1
    
    Summary: 
             Bitcoin is a form of digitial currency, otherwise known as cryptocurrency. 
             Rather than rely on a central authority like a bank, 
             Bitcoin instead relies on a distributed network, 
             otherwise known as a blockchain, to record transactions.

            Because there’s demand for Bitcoin (i.e., users want it), 
            users are willing to buy it, as by exchanging one currency (e.g., USD) for Bitcoin.

            In a file called bitcoin.py, implement a program that:

            Expects the user to specify as a command-line argument the number of Bitcoins, 
            , that they would like to buy. If that argument cannot be converted to a float, 
            the program should exit via sys.exit with an error message.
            Queries the API for the CoinDesk Bitcoin Price Index at 
            https://api.coindesk.com/v1/bpi/currentprice.json, 
            which returns a JSON object, among whose nested keys is the current price of Bitcoin as a float. 
            Be sure to catch any exceptions, as with code like:
            import requests

            try:
                ...
            except requests.RequestException:
                ...
                
            Outputs the current cost of Bitcoins 
            in USD to four decimal places, using , as a thousands separator.
"""
import requests, sys


API_URL = "https://api.coindesk.com/v1/bpi/currentprice.json"

def main():
    # program requires a numeric as command-line argument
    if validate_cl_arguments():
        bitcoin_amount = validate_cl_arguments()
        # request the current bitcoin rate from an API
        current_usd_rate = request_bitcoin_api(API_URL)
        # calculate the price for the given input based on current rate
        price = current_usd_rate * bitcoin_amount
        # outputs the total price for the user in USD 
        print(f"${price:,.4f}") # to four decimal places, using , as a thousands separator. 
        

def validate_cl_arguments():
    if len(sys.argv) != 2:
        sys.exit("Missing command-line argument.")
    else:
        try:
            return float(sys.argv[1])
        
        except ValueError:
            sys.exit("Command-line argument is not a number.")


def request_bitcoin_api(URL: str) -> float:
    """requests the current bitcoin api and returns the current bitcoin rate."""
    try:
        # request the price for the given amount of bitcoin
        r = requests.get(API_URL)
        # dumps the json response into a python dictionary
        data = r.json()
        # extract the current bitcoin price (in USD) into a variable as numeric value
        usd_rate = data['bpi']['USD']['rate']
        # remove the comma from the string before converting to a float
        return float(usd_rate.replace(',', ''))
            
    except (requests.exceptions.JSONDecodeError, requests.RequestException):
        sys.exit("Request failed. Try again later.")    





if __name__ == '__main__':
    main()
    
    

"""Here’s how to test your code manually:

Run your program with python bitcoin.py. 
Your program should use sys.exit to exit with an error message:
    Missing command-line argument   

Run your program with python bitcoin.py cat. 
Your program should use sys.exit to exit with an error message:
    Command-line argument is not a number

Run your program with python bitcoin.py 1. 
Your program should output the price of a single Bitcoin 
to four decimal places, using , as a thousands separator.

Run your program with python bitcoin.py 2. 
Your program should output the price of two Bitcoin 
to four decimal places, using , as a thousands separator.

Run your program with python bitcoin.py 2.5. 
Your program should output the price of 2.5 Bitcoin 
to four decimal places, using , as a thousands separator.
"""

"""check50 cs50/problems/2022/python/bitcoin"""