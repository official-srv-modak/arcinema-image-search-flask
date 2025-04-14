import ollama


directory="uploads/"
import requests

import requests


def read_image_and_get_movie_name(post_name):
	print(post_name)
	res = ollama.chat(
		model="llava",
		messages=[
			{
				'role': 'user',
				# 'content': 'Just give me the name of the movie in the poster. NO SENTENCES just ONE PHRASE in the format MOVIE_NAME (RELEASE_YEAR). Dont forget the release year in brackets. Just the name of the poster if it is not poster then say NULL.',
				# 'content': 'Just give me the name of the movie in the poster. NO SENTENCES just ONE PHRASE in the format MOVIE_NAME (RELEASE_YEAR). Dont forget the release year in brackets. '
				# 		   'If recognised refer to my list movie name='+movie_names_str+' and tell me which one from the list'
				# 																				 'Just the name of the poster if it is not poster then say NULL.',
				'content': (
					"You are given a poster image of a movie. Your task is to identify the movie name. "
					"Respond strictly in one of the following formats:\n\n"
					"1. MOVIE_NAME (RELEASE_YEAR) — if the movie is in the list provided below.\n"
					"2. NULL — if the image is not a movie poster or cannot be matched.\n\n"
					# "Only use the movie names provided below (case-insensitive match is fine):\n"
					# f"{movie_names_str}\n\n"
					"STRICT FORMAT: Only return the exact matched name in format MOVIE_NAME (RELEASE_YEAR) or NULL. "
					"Do not add any explanation or text."
					"3. Don't use any special characters like semicolon even if actual movie name has it."
				),

				'images': [directory + post_name]
			}
		]
	)
	print("Found movie name : " + res['message']['content'])
	return res['message']['content']

def get_movie_name():
	get_url = 'http://10.0.0.47:8089/arcinema-image-search/get-movies'
	try:
		get_response = requests.get(get_url)
		get_response.raise_for_status()
		json_data = get_response.json()

		# Step 2: Extract movie names
		movie_names = [item["movieName"] for item in json_data.get("url", []) if "movieName" in item]
		movie_names_str = ", ".join(movie_names)

		print(f"Extracted movie names: {movie_names_str}")

	except requests.exceptions.RequestException as e:
		print(f"GET request failed: {e}")
		return "NULL"
	except ValueError:
		print("Failed to parse JSON.")
		return "NULL"

# print(read_image_and_get_movie_name("POSTER.png"))