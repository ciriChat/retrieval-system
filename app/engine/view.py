from flask import Blueprint, jsonify, request

from app.engine.feminine_converter import MessageToFeminineFormConverter
from app.engine.message import MessageFactory
from app.engine.service import EngineService

blueprint = Blueprint('chat', __name__)


@blueprint.route("/chat", methods=['PUT'])
def chat():
    msg = request.json['message']
    response = EngineService.get_response(msg)
    return jsonify(message=response)


@blueprint.route("/feminine", methods=['PUT'])
def to_feminine():
    msg = request.json['message']
    msg_obj = MessageFactory.from_text_msg(msg)
    resp = MessageToFeminineFormConverter.convert(msg_obj)
    return jsonify(message=resp.text)