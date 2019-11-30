from flask import jsonify
from app import app
from app.crawler import notices

@app.route("/")
def index():
    return "Hello World"

@app.route("/noticias", defaults={'page':1}, methods=['GET'])
@app.route("/noticias/<int:page>")
def getNoticias(page):
    all_notices = notices.get_articles(page)
    return jsonify(all_notices)
