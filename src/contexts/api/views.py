from flask import Blueprint, jsonify
from src.contexts.integration.ifba.main.factories.controllers.get_posts_controller_factory import \
    make_get_posts_controller

bp_views = Blueprint('views', __name__)


@bp_views.route("/", defaults={'page': 1}, methods=['GET'])
@bp_views.route("//<int:page>")
def get_noticias(page):
    all_notices = make_get_posts_controller().handler()
    return jsonify(all_notices)
