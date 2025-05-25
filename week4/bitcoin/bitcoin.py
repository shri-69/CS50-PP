import sys
import requests

def main():

    if len(sys.argv) != 2:
        sys.exit("Usage: python bitcoin.py <number_of_bitcoins>")


    try:
        bitcoins = float(sys.argv[1])
    except ValueError:
        sys.exit("Error: Argument must be a number.")


    url = "https://rest.coincap.io/v3/assets/bitcoin"
    headers = {
        "Authorization": "Bearer a26e7f13b245ba796618468ef77310bb308fefeda0592ef953bf7ac8d66821d4"
    }

    #
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        data = response.json()
        price = float(data["data"]["priceUsd"])
    except requests.RequestException:
        sys.exit("Error: Failed to fetch data from CoinCap.")
    except (KeyError, ValueError):
        sys.exit("Error: Unexpected response format from API.")


    total_cost = bitcoins * price
    print(f"${total_cost:,.4f}")

if __name__ == "__main__":
    main()
