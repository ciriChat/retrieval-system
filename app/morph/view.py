from flask import Blueprint, jsonify, request
from functional import seq

from app.subtitle.tokenizer import SimpleTokenizer
from .service import MorphService

blueprint = Blueprint('morph', __name__)


@blueprint.route("/morph", methods=['PUT'])
def hello():
    token = request.json['token'].lower()
    token = MorphService.get_morph_token(token)
    return jsonify(token=token, base_form=token.base_form, tags=token.tags.tags)


@blueprint.route("/language/check/polish", methods=['PUT'])
def check_polish():
    msg = request.json['message']
    tokens = SimpleTokenizer.tokenize(msg)

    morph_tokens = seq(MorphService.get_morph_tokens(tokens)).filter(lambda t: t.tags).to_list()

    if len(morph_tokens) / len(tokens) > .5:
        return jsonify(polish=True)
    return jsonify(polish=False)
