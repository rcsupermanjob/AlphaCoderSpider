from flask import Flask, request, render_template, jsonify
from AlphaCoderSpider.spider import search as search_img
from AlphaCoderSpider.config import get_content, delete_create

app = Flask(__name__)


def web_start(host, port):
    app.run(host=host, port=port)


@app.route('/new', methods=['GET'])
def new():
    dynamic_ = get_content()
    delete_create()
    if dynamic_:
        return jsonify(dynamic_)
    else:
        return jsonify(' ')


@app.route('/', methods=['GET'])
def hello():
    return render_template('index.html')


@app.route('/search/<keyword>')
def search(keyword):
    if request.referrer:
        search_img(keyword)
        return render_template('search.html', keyword=keyword)
    else:
        return render_template('404.html')


