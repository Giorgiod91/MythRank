import os
import requests
from dotenv import load_dotenv
import json

# Correct the URL
tokenURL = "https://www.warcraftlogs.com/oauth/token"

def get_token(store: bool = True):
    # Prepare data for the request
    data = {"grant_type": "client_credentials"}
    auth = (os.environ.get("CLIENT_ID"), os.environ.get("CLIENT_SECRET")) 

    # Send POST request to get the token
    with requests.Session() as session:
        response = session.post(tokenURL, data=data, auth=auth)
    # if the status code equals 200 store the response as the store token
    if store and response.status_code == 200: 
        store_token(response)

    return response

def store_token(response):
    try:
        # Save the token to a file
        with open(".credentials.json", mode="w+", encoding="utf-8") as f:
            json.dump(response.json(), f)
    except OSError as e:
        print(f"Error saving token: {e}")
        return None

def read_token():
    try:
        # Read the token from the file
        with open(".credentials.json", mode="r", encoding="utf-8") as f:
            access_token = json.load(f)
            return access_token
    except OSError as e:
        print(f"Error reading token: {e}")
        return None

def main():
    # Request the token and print the response
    response = get_token()
    if response.status_code == 200:
        print("Token received successfully:")
        print(response.json())
    else:
        print(f"Failed to get token. Status code: {response.status_code}")
        print(response.json())

# Run the main 
if __name__ == "__main__":
    main()
