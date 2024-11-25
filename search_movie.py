import requests
import json

# Load API key and CSE ID from the external JSON file
def load_config():
    with open('config.json') as config_file:
        config = json.load(config_file)
    return config['api_key'], config['cse_id']

def get_movie_trailer(movie_name):
    # Load the API key and CSE ID
    api_key, cse_id = load_config()

    search_query = f"{movie_name} trailer site:youtube.com"
    print("Search for movie: " + movie_name)
    url = f"https://www.googleapis.com/customsearch/v1?q={search_query}&key={api_key}&cx={cse_id}"

    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()

        # Loop through the search results to find YouTube links
        for item in data.get('items', []):
            link = item.get('link')
            if "youtube.com" in link:
                return link
    return "Trailer not found."
