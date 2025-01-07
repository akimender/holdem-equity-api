import json
from flask import Flask, request, jsonify
from src.calculate import get_equity

app = Flask(__name__)

@app.route("/")
def index():
    return jsonify({'name': 'alice2',
                    'email': 'alice@outlook.com'})

@app.route('/calculate-equity', methods=['POST'])
def calculate_equity():
    data = request.get_json()
    result = get_equity(data)

    try:
        return jsonify({
            "message": "Calculation Complete!",
            "equity": result
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(port=8000, debug=True)