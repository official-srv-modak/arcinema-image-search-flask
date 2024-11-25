import ollama


directory="uploads/"
def read_image_and_get_movie_name(post_name):
	print(post_name)
	res = ollama.chat(
		model="llava",
		messages=[
			{
				'role': 'user',
				'content': 'Just give me the name of the movie in the poster i gave you. no jibber jabbar just the name of the poster if it is not poster then say NULL. no sentence just in the format in the format MOVIE_NAME (RELEASE_YEAR)',
				'images': [directory + post_name]
			}
		]
	)
	print("Found movie name : "+res['message']['content'])
	return res['message']['content']

# print(read_image_and_get_movie_name("poster1.jpg"))