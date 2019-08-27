from flask import Flask, jsonify
from AlphaCoderSpider.spider import links

app = Flask(__name__)


def web_start(host, port):
    app.run(host=host, port=port)


@app.route('/')
def index():
    return jsonify(links)
