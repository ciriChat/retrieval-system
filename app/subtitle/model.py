from ..db import db
from sqlalchemy.sql import text


class Subtitle(db.Model):
    __tablename__ = 'subtitle_pl'
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(1000), nullable=False)
    start = db.Column(db.Integer)
    stop = db.Column(db.Integer)
    hash1 = db.Column(db.String(50))
    hash2 = db.Column(db.String(100))
    hash3 = db.Column(db.String(150))


class SubtitleRepository:
    SELECT_RANDOM_HASH = '''
        SELECT s.text 
        FROM subtitle_pl s 
        WHERE {} = :hash 
        ORDER BY 
        RAND() 
        LIMIT 20
    '''

    SELECT_RANDOM_HASH_NEXT = '''
       SELECT s.text 
       FROM subtitle_pl s 
       WHERE s.id IN (
           SELECT id + 1
           FROM subtitle_pl 
           WHERE {} = :hash 
           ORDER BY RAND() 
       )
       LIMIT 50 
    '''

    @classmethod
    def find_by_hash1(cls, hash1):
        return db.engine.execute(cls._select_random_query('hash1'), {'hash': hash1})

    @classmethod
    def find_by_hash2(cls, hash2):
        return db.engine.execute(cls._select_random_query('hash2'), {'hash': hash2})

    @classmethod
    def find_by_hash3(cls, hash3):
        return db.engine.execute(cls._select_random_query('hash3'), {'hash': hash3})

    @classmethod
    def find_next_by_hash1(cls, hash1):
        return db.engine.execute(cls._select_random_next_query('hash1'), {'hash': hash1})

    @classmethod
    def find_next_by_hash2(cls, hash2):
        return db.engine.execute(cls._select_random_next_query('hash2'), {'hash': hash2})

    @classmethod
    def find_next_by_hash3(cls, hash3):
        return db.engine.execute(cls._select_random_next_query('hash3'), {'hash': hash3})

    @classmethod
    def _select_random_query(cls, hash_column):
        return text(cls.SELECT_RANDOM_HASH.format(hash_column))

    @classmethod
    def _select_random_next_query(cls, hash_column):
        return text(cls.SELECT_RANDOM_HASH_NEXT.format(hash_column))
