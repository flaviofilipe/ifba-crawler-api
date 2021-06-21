from flask import Blueprint, jsonify, request
from src.contexts.integration.ifba.main.factories.controllers.get_posts_controller_factory import \
    make_get_posts_controller

bp_views = Blueprint('views', __name__)


@bp_views.route("/", methods=['GET'])
def get_noticias():
    page = request.args.get('page')
    page = int(page) if page else 1
    all_notices = make_get_posts_controller().handler(page)
    return jsonify(all_notices)
