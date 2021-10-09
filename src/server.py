from flask import Flask, request, jsonify
from waitress import serve
import gcld3

app = Flask(__name__)
detector = gcld3.NNetLanguageIdentifier(min_num_bytes=20, max_num_bytes=1000)

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json
    tasks = data.get("tasks")
    results = []
    for text in tasks:
        result = detector.FindLanguage(text=text)
        results.append({
            "language": result.language,
            "isReliable": result.is_reliable,
            "proportion": result.proportion,
            "probability": result.probability
        })
    return jsonify({"results": results})


if __name__ == "__main__":
    serve(app, host='0.0.0.0', port=9000)
