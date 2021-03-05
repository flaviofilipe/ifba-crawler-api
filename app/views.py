from flask import Blueprint, jsonify, current_app, request
from app.crawler import notices

bp_views = Blueprint('views', __name__)


@bp_views.route("/")
def index():
    return "Hello World"


@bp_views.route("/noticias", defaults={'page': 1}, methods=['GET'])
@bp_views.route("/noticias/<int:page>")
def get_noticias(page):
    all_notices = notices.get_articles(page)
    return jsonify(all_notices)
