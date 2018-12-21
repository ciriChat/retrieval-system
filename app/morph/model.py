from enum import Enum
from typing import List

from ..db import db


class MorphRecord(db.Model):
    __tablename__ = 'morph_dict_pl_2'
    id = db.Column(db.Integer, primary_key=True)
    word = db.Column(db.String(50), nullable=False)
    base_form = db.Column(db.String(50), nullable=False)
    tags = db.Column(db.String(50), nullable=False)


class MorphRepository:
    @classmethod
    def find_by_word(cls, word: str) -> MorphRecord:
        return MorphRecord.query.filter(MorphRecord.word == word).first()

    @classmethod
    def find_word_by_tags(cls, base_form: str, tags: str) -> MorphRecord:
        return MorphRecord.query \
            .filter(MorphRecord.base_form == base_form, MorphRecord.tags == tags) \
            .first()


class GrammaticalClass(Enum):
    subst = 1
    depr = 2
    num = 3
    numcol = 4
    adj = 5
    adja = 6
    adjp = 7
    adjc = 8
    adv = 9
    ppron12 = 10
    ppron3 = 11
    siebie = 12
    fin = 13
    bedzie = 14
    aglt = 15
    praet = 16
    impt = 17
    imps = 18
    inf = 19
    pcon = 20
    pant = 21
    ger = 22
    pact = 23
    ppas = 24
    winien = 25
    pred = 26
    prep = 27
    conj = 28
    comp = 29
    qub = 30
    brev = 31
    burk = 32
    interj = 33
    interp = 34
    xxx = 35
    ign = 36


class GrammaticalNumber(Enum):
    sg = 1
    pl = 2


class GrammaticalCase(Enum):
    nom = 1
    gen = 2
    dat = 3
    acc = 4
    inst = 5
    loc = 6
    voc = 7


class GrammaticalGender(Enum):
    m1 = 1
    m2 = 2
    m3 = 3
    f = 4
    n = 5


class GrammaticalPerson(Enum):
    pri = 1
    sec = 2
    tri = 3


class GrammaticalGrade(Enum):
    pos = 1
    com = 2
    sup = 3


class GrammaticalAspect(Enum):
    imperf = 1
    perf = 2


class GrammaticalNegation(Enum):
    aff = 1
    neg = 2
