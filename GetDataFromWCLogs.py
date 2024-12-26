import os
import requests
from dotenv import load_dotenv
import json

#URLS
tokenURL = "https://www.warcraftlogs.com/oauth/token"
publicAPI = "https://www.warcraftlogs.com/api/v2/client"

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
            return access_token['access_token']  # Ensure to return only the access token
    except OSError as e:
        print(f"Error reading token: {e}")
        return None
    
def retrive_headers()->dict[str, str]:
    token = read_token()
    if token:
        return {"Authorization": f"Bearer {token}"}
    else:
        return {}

# querys to fetch from wclogs API
query = """
query($name: String, $serverSlug: String, $serverRegion: String) {
    characterData {
        character(name: $name, serverSlug: $serverSlug, serverRegion: $serverRegion) {
            id
            name
            server {
                name
                slug
            }
        }
    }
}
"""

#query to get the logs connected with the player id
query2 = """
            """
#function to get player from user input for now later will be automated or something 

def get_player():
    name = input("Enter The Character Name: ")
    serverSlug = input("Enter The Server Name: ")
    serverRegion = input("Which Region is the Player on? Type 'eu' or 'na': ")
    return {"name": name, "serverSlug": serverSlug, "serverRegion": serverRegion}

def get_data(query: str, variables: dict):
    data = {"query": query, "variables": variables}
    with requests.Session() as session:
        session.headers = retrive_headers()  
        response = session.post(publicAPI, json=data)  # POST method to send GraphQL query
        return response.json()
    

#function save the player id with the  given name and so on cause i later need the player id to give out the score and also i use the id for my own api that ppl can fetch with the id

def save_player_id(player_data):
    try:
        # Fetch character data
        response = get_data(query, player_data)

        # Check if the necessary data exists in the response go through the data basically from data then charackterData
        character = response.get("data", {}).get("characterData", {}).get("character", {})

        # Extract the player ID and name
        player_id = character.get("id")
        player_name = character.get("name")

        # If ID and name are found, save them to the file
        if player_id and player_name:
            with open(".ids", mode="w+", encoding="utf-8") as f:
                json.dump({"name": player_name, "id": player_id}, f)
            print(f"Player ID {player_id} and name {player_name} saved successfully.")
        else:
            print("Player ID or name not found in the response.")

    except Exception as e:
        print(f"Error saving player ID: {e}")


# get the logs from a player with player id those i need to train my model later

def get_logs(id, query: str, variables: dict):
    data = {"query": query2, "variables": variables}
    with requests.Session() as session:
        session.headers = retrive_headers()  
        response = session.post(publicAPI, json=data)
        return response.json()
    
# function to save the logs in a seperate file for my training model



        





def main():
    # Request the token and print the response
    response = get_token()
    if response.status_code == 200:
        print("Token received successfully:")
        print(response.json())
    else:
        print(f"Failed to get token. Status code: {response.status_code}")
        print(response.json())

    # Get player data from input
    player_data = get_player()

    # Fetch character data using the corrected query
    trainingData = get_data(query, player_data)

    #call the save function
    save_player_id(player_data)

    # Print the fetched data
    print(json.dumps(trainingData, indent=2))


if __name__ == "__main__":
    main()
