from flask import Flask, jsonify, request
from for_interfaces import html_code
import requests
import emoji

app = Flask(__name__)


@app.route("/oracle-1", methods=['GET', 'POST'])
def send_back_html():
    # return html post to controller
    print("sending html form to controller")
    return html_code


@app.route("/oracle-2", methods=['GET', 'POST'])
def convert_http_to_gitcoin():
    # map
    text = request.get_data().decode("utf-8")
    print("got text: ", text)
    return "hi there"


@app.route("/oracle-3", methods=['GET', 'POST'])
def some_func():
    # add something here
    return "bla"


@app.route("/oracle-4", methods=['GET', 'POST'])
def some_other_func():
    # add something here
    return "fin"


if __name__ == '__main__':
    app.run(debug=True, port=5001)
