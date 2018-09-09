from flask import Flask, jsonify, request
from for_interfaces import html_code
from eth_raw_tx_bounty import raw_tx

app = Flask(__name__)


@app.route("/oracle-1", methods=['GET', 'POST'])
def send_back_html():
    # return html post to controller
    print("sending html form to controller")
    return html_code


@app.route("/gitcoin-bounty", methods=['GET', 'POST'])
def convert_http_to_gitcoin():
    emoji_map = {
        "&#x1F41B": "asdf",
        "&#x1F31F": "lkjh",
        "&#x1F477": "poiu",
        "&#x1F3C3": "xcvb",
    }
    text = request.get_data(as_text=True)
    processed = text.replace("+%26%23", " &#")
    received_emojis = processed.split(" ")[1:]
    git_coin_attribute = []
    for emoji in received_emojis:
        try:
            git_coin_attribute.append(emoji_map.get(emoji))
        except Exception:
            pass
    print("emojis: ", received_emojis)
    print("list of gitcoin attributes: ", git_coin_attribute)
    return jsonify(git_coin_attribute)


@app.route("/oracle-raw-tx", methods=['GET', 'POST'])
def send_back_raw_tx():
    return raw_tx()


@app.route("/oracle-4", methods=['GET', 'POST'])
def some_other_func():
    # add something here
    return "gitcoin bounty successfully deployed"


if __name__ == '__main__':
    app.run(debug=True, port=5001)
