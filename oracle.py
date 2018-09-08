from flask import Flask, jsonify

app = Flask(__name__)

# See http://flask.pocoo.org/snippets/57/
@app.route('/', defaults={'path': ''}, methods=['POST'])
@app.route('/<path:path>', methods=['POST'])

def catch_all(path):
    return "Hi"
    
if __name__ == '__main__':
    app.run(debug=True)