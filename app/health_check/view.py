from flask import Blueprint, request, jsonify

blueprint = Blueprint('health_check', __name__)


@blueprint.route("/", methods=['GET'])
def get_similar():
    return jsonify({
        'message': 'hello'
    })
