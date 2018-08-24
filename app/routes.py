from flask import Flask, jsonify, request

app = Flask('__name__')

questions = []

@app.route('/questions', methods=['POST'])
def ask_question():
    data = request.get_json()
    title = data.get("title")
    body = data.get("body")

    if body and title:
        return jsonify({"message": "question posted"})
    else:
        return jsonify({"message": "not posted"})

@app.route('/questions/<question_id>', methods=['GET'])
def get_one_question():
    