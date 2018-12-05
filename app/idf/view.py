from flask import Blueprint, jsonify, request
from .model import IdfPlRepository

blueprint = Blueprint('idf', __name__)


@blueprint.route("/idf", methods=['PUT'])
def hello():
    word = request.json['word'].lower()
    value = IdfPlRepository.find_idf(word)
    return jsonify(value=value)
