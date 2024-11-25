import ollama


directory="uploads/"
def read_image_and_get_movie_name(post_name):
	print(post_name)
	res = ollama.chat(
		model="llava",
		messages=[
			{
				'role': 'user',
				'content': 'Just give me the name of the movie in the poster. NO SENTENCES just ONE PHRASE in the format in the format MOVIE_NAME (RELEASE_YEAR). Just the name of the poster if it is not poster then say NULL.',
				'images': [directory + post_name]
			}
		]
	)
	print("Found movie name : "+res['message']['content'])
	return res['message']['content']

# print(read_image_and_get_movie_name("poster1.jpg"))