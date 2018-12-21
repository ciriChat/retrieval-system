import random
from typing import List
from functional import seq

from app.emotions.service import EmotionsService, EmoticonFactory
from app.engine.feminine_converter import MessageToFeminineFormConverter
from app.engine.message import MessageFactory, Message
from app.subtitle.service import SubtitleService


class EngineService:
    @classmethod
    def get_response(cls, msg) -> str:
        response = SubtitleService.find_next_subs_by_idf(msg)
        response_obj = MessageFactory.from_text_msg(random.choice(response))
        emotion = EmotionsService.get_emotions_for_msg(response_obj)
        emoticon = EmoticonFactory.create_emoticon(emotion)

        feminine_response = MessageToFeminineFormConverter.convert(response_obj)

        if emoticon:
            return feminine_response.text + ' ' + emoticon
        return feminine_response.text

    def _select_msg(self, msgs: List[str]) -> Message:
        msgs_obj = seq(msgs).map(MessageFactory.from_text_msg).to_list()

        rejected = []
        ok = []

        for msg in msgs_obj:
            for token in msg.morph_tokens:
                if not token.base_form:
                    rejected.append(msg)
                    break
            ok.append(msg)

