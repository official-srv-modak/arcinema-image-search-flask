import requests



# Usage example
api_key = 'AIzaSyD2XfbI3qgPXme7Hr-BaiFh4OOqozkqx1w'  # Replace with your API key
cse_id = 'c32ee9c562abe4e76'  # Replace with your Custom Search Engine ID

def get_movie_trailer(movie_name):
    search_query = f"{movie_name} trailer site:youtube.com"
    print("Search for movie : "+movie_name)
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

# movie_name = input("Enter the movie name: ")
# trailer_link = get_movie_trailer(movie_name)
# print(f"Trailer link: {trailer_link}")
