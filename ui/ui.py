from flask import Flask
app = Flask(__name__)

html = """
<input type="text" value="This is some text" id="text" style="width: 150px;" />
<br />
<input type="button" value="Click Me" id="button" />
"""

@app.route("/")
def hello():
    return html


if __name__ == '__main__':
    app.run(debug=True)
