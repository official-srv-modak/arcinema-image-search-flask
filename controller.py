from flask import Flask, request, jsonify
import os
from werkzeug.utils import secure_filename

import requests
from bs4 import BeautifulSoup

from flask_cors import CORS

from search_movie import get_movie_trailer
from test_image_ollama import read_image_and_get_movie_name

app = Flask(__name__)
CORS(app)

# Configure the upload folder and allowed extensions
UPLOAD_FOLDER = os.path.join(os.path.dirname(__file__), 'uploads')
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Ensure the upload directory exists
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


def allowed_file(filename):
    """Check if the uploaded file has an allowed extension."""
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/upload', methods=['POST'])
def upload_image():
    """Endpoint to upload an image."""
    if 'file' not in request.files:
        return jsonify({'error': 'No file part in the request'}), 400

    file = request.files['file']

    if file.filename == '':
        return jsonify({'error': 'No file selected'}), 400

    if file and allowed_file(file.filename):
        # Use secure_filename to prevent directory traversal attacks
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)
        return jsonify({'message': 'File uploaded successfully', 'file_name': filename}), 200
    else:
        return jsonify({'error': 'File type not allowed'}), 400

@app.route('/get-url', methods=['POST'])
def get_trailer_url():
    data = request.json
    name = data["image_name"]
    movie_name = read_image_and_get_movie_name(name)
    if "NULL" not in movie_name:
        url = get_movie_trailer(movie_name)
        return jsonify({'url': url}), 200
    else:
        return jsonify({'error': 'Image doesn\'t seem to be of a movie poster'}), 200



if __name__ == '__main__':
    app.run(debug=True, port=8888, host="0.0.0.0")
