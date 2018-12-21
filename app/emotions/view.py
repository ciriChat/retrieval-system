from flask import Blueprint, jsonify, request

from app.emotions.service import EmotionsService, EmoticonFactory
from app.engine.message import MessageFactory

blueprint = Blueprint('emotions', __name__)


@blueprint.route("/emotions", methods=['PUT'])
def to_feminine():
    msg = request.json['message']
    msg_obj = MessageFactory.from_text_msg(msg)
    emotion = EmotionsService.get_emotions_for_msg(msg_obj)
    emoticon = EmoticonFactory.create_emoticon(emotion)
    return jsonify(happiness=emotion.happiness, fear=emotion.fear, anger=emotion.anger, sadness=emotion.sadness, disgust=emotion.disgust, emoticon=emoticon)