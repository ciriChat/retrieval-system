from ..db import db


class EmotionsRecord(db.Model):
    __tablename__ = 'emotions_pl'
    word = db.Column(db.String(50), primary_key=True)
    category = db.Column(db.String(2), nullable=True)
    happiness = db.Column(db.Float, nullable=False)
    anger = db.Column(db.Float, nullable=False)
    sadness = db.Column(db.Float, nullable=False)
    fear = db.Column(db.Float, nullable=False)
    disgust = db.Column(db.Float, nullable=False)


class EmotionsRepository:
    @classmethod
    def find_emotions(cls, word: str) -> EmotionsRecord:
        return EmotionsRecord.query.filter(EmotionsRecord.word == word).first()
