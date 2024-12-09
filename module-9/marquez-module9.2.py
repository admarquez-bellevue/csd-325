import requests
 
url = "https://pokeapi.co/api/v2/pokemon/"

def main():
    # Make request to API
    print("Testing the API connection.")
    response = requests.get(url)

    # Print status code
    print("Status Code:", response.status_code)

    if response.status_code == 200:
        print("Connection Success")

        # Print raw data
        print("\nNon-formatted Response:")
        print(response.text)

        # Print formatted data
        data = response.json()
        print("\nFormatted Response:")
        print("\nPokemon List (First 15):\n")
        for result in data['results'][:15]:
            print(f"{result['name'].capitalize()}")
    else:
        print("Connection Failed")

if __name__ == "__main__":
    main()

