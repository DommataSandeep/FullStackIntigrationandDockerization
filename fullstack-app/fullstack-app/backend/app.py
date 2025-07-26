from flask import Flask, request, jsonify
from flask_cors import CORS
app = Flask(__name__)
CORS(app)
messages = []
@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    user_msg = data.get('message')
    messages.append({'user': user_msg, 'ai': 'Hello! This is AI.'})
    return jsonify({'response': 'Hello! This is AI.'})
@app.route('/history', methods=['GET'])
def history():
    return jsonify(messages)
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)