import os
import json

import vertexai
from vertexai.preview.generative_models import GenerativeModel, Part

from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['POST'])
def generate_text():
    dumps = {}

    if request.get_json():
        dumps = json.dumps(request.get_json())
        dumps = json.loads(dumps)

    configuration = {
        "project": [dumps["project"]],
        "location": [dumps["location"]],
        "picture": [dumps["picture"]],
    }

    #Initialize Vertex AI
    vertexai.init(project=configuration["project"], location=configuration["project"])

    # Load the model
    multimodal_model = GenerativeModel("gemini-pro-vision")

    # Query the model
    response = multimodal_model.generate_content(
        [
            # Add an example image
            Part.from_uri(
                configuration["picture"]
            ),
            # Add an example query
            "give me the gcloud commands to provision this architecture?",
        ]
    )

    response.headers.add('Access-Control-Allow-Origin', '*')

    return response

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))