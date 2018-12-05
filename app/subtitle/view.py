from flask import Blueprint, jsonify, request

from .service import SubtitleService

blueprint = Blueprint('subtitles', __name__)


@blueprint.route("/subtitles/similar", methods=['PUT'])
def get_similar():
    msg = request.json['message'].lower()
    msgs = SubtitleService.find_similar_subs_by_idf(msg)
    return jsonify(messages=msgs)


@blueprint.route("/subtitles/next", methods=['PUT'])
def get_next():
    msg = request.json['message'].lower()
    msgs = SubtitleService.find_next_subs_by_idf(msg)
    return jsonify(messages=msgs)