from typing import List

from functional import seq

from app.morph.model import MorphRecord
from app.morph.model import MorphRepository


class MorphTags:
    TAG_SEPARATOR = ':'
    NESTED_TAG_SEPARATOR = '.'

    def __init__(self, tags: str):
        self.tags = tags

    def is_verb(self) -> bool:
        return 'verb:' in self.tags

    def is_singular(self):
        return ':sg:' in self.tags

    def is_first_person(self) -> bool:
        return ':pri:' in self.tags

    def is_feminine(self) -> bool:
        return ':f' in self.tags or '.f' in self.tags

    def is_masculine(self) -> bool:
        return 'm1' in self.tags or 'm2' in self.tags or 'm3' in self.tags

    def get_tags(self) -> List[str]:
        return self.tags.split(self.TAG_SEPARATOR)


class MorphToken:
    def __init__(self, token: str, base_form: str = None, tags: MorphTags = None):
        self.token = token
        self.base_form = base_form
        self.tags = tags


class MorphTokenFactory:
    @classmethod
    def from_morph_record(cls, token, morph_record: MorphRecord) -> MorphToken:
        if not morph_record:
            return MorphToken(token)
        tags = MorphTags(morph_record.tags)
        return MorphToken(morph_record.word, morph_record.base_form, tags)


class MorphService:
    @classmethod
    def get_morph_token(cls, token: str) -> MorphToken:
        return MorphTokenFactory.from_morph_record(token, MorphRepository.find_by_word(token))

    @classmethod
    def get_morph_tokens(cls, tokens: List[str]) -> List[MorphToken]:
        return seq(tokens).map(cls.get_morph_token).to_list()
