from flask import Flask, request
import requests
import os
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
API_KEY = os.getenv("NEWSAPI_KEY")

@app.route('/news', methods=['GET'])
def get_news():
    parameters = {
        'country': request.args.get('country'),
        'category': request.args.get('category'),
        'q': request.args.get('q'),
        'sources': request.args.get('sources'),
        'from': request.args.get('from_param'),
        'to': request.args.get('to'),
        'sort_by': request.args.get('sort_by'),
        'apiKey': API_KEY
    }

    # Remove parameters that are None
    parameters = {k: v for k, v in parameters.items() if v is not None}

    url = "https://newsapi.org/v2/top-headlines"
    response = requests.get(url, params=parameters)

    return response.json()

if __name__ == '__main__':
    app.run(debug=True)
