from flask import Flask, jsonify, request
from for_interfaces import html_code
import requests

app = Flask(__name__)


@app.route("/oracle-1", methods=['GET', 'POST'])
def send_back_html():
    # return html post to controller
    return html_code


@app.route("/oracle-2", methods=['GET', 'POST'])
def make_http_post():
    requests.post(url="some url", data="some data")


@app.route("/oracle-3", methods=['GET', 'POST'])
def add_message():
    # add something here
    pass


@app.route("/oracle-4", methods=['GET', 'POST'])
def add_message():
    # add something here
    pass


if __name__ == '__main__':
    app.run(debug=True, port=5001)
