from app.emotions.model import EmotionsRecord, EmotionsRepository
from app.engine.message import Message
from functional import seq
from typing import List


class Emotion:
    def __init__(self, happiness=1., anger=1., sadness=1., fear=1., disgust=1.):
        self.happiness = happiness
        self.anger = anger
        self.sadness = sadness
        self.fear = fear
        self.disgust = disgust


class EmotionFactory:
    @staticmethod
    def from_emotions_record(emotions_record: EmotionsRecord) -> Emotion or None:
        if not emotions_record:
            return None
        return Emotion(emotions_record.happiness, emotions_record.anger, emotions_record.sadness, emotions_record.fear,
                       emotions_record.disgust)


class EmoticonFactory:
    HAPPY = ':)'
    ANGRY = ':('
    SAD = ":'("
    AFRAID = 'D='
    DISGUSTED = 'D;'

    @classmethod
    def create_emoticon(cls, emotion: Emotion) -> str or None:
        emotions = seq((emotion.happiness, cls.HAPPY), (emotion.anger, cls.ANGRY), (emotion.sadness, cls.SAD), (emotion.fear, cls.AFRAID), (emotion.disgust, cls.DISGUSTED)) \
            .sorted(lambda e: e[0], True).to_list()

        if emotions[0][0] > 2.5:
            return emotions[0][1]
        return None


class EmotionsService:
    @classmethod
    def get_emotions(cls, word: str) -> Emotion:
        return EmotionFactory.from_emotions_record(EmotionsRepository.find_emotions(word))

    @classmethod
    def get_emotions_for_msg(cls, msg: Message) -> Emotion:
        emotions = seq(msg.morph_tokens).map(lambda t: t.base_form).map(cls.get_emotions).filter(lambda e: e).to_list()
        return cls._emotions_mean(emotions)

    @classmethod
    def _emotions_mean(cls, emotions: List[Emotion]) -> Emotion:
        happiness = 0.0
        anger = 0.0
        sadness = 0.0
        fear = 0.0
        disgust = 0.0

        for emotion in emotions:
            happiness += emotion.happiness
            anger = emotion.anger
            sadness = emotion.sadness
            fear = emotion.fear
            disgust = emotion.disgust

        size = len(emotions)
        if size < 1:
            return Emotion()
        return Emotion(happiness/size, anger/size, sadness/size, fear/size, disgust/size)

