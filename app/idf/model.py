from ..db import db


class IdfPl(db.Model):
    __tablename__ = 'idf_pl'
    word = db.Column(db.String(50), primary_key=True)
    value = db.Column(db.Float, nullable=False)


class IdfPlRepository:
    @staticmethod
    def find_idf(word: str) -> float:
        value = IdfPl.query.with_entities(IdfPl.value).filter(IdfPl.word == word).first()
        if value:
            return value[0]
        return 0
