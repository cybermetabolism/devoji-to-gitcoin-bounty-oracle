from flask import Flask, jsonify, request

app = Flask(__name__)
response = "Oracle: I received your message - now working on it!"


@app.route('/post/<uuid>', methods=['GET', 'POST'])
def add_message(uuid):
    content = request.get_data()
    print("content: ", content)
    return response


if __name__ == '__main__':
    app.run(debug=True)
