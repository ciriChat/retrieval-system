from typing import List, Sequence
from ..idf.service import IdfService
from .tokenizer import SimpleTokenizer
from functional import seq


class HashFactory:
    HASH_SEPARATOR = '_'

    @classmethod
    def get_hash(cls, tokens: Sequence[str]):
        return cls.HASH_SEPARATOR.join(tokens)


class IdfHashFactory:
    class MsgToken:
        def __init__(self, index, token, idf):
            self.index = index
            self.token = token
            self.idf = idf

    @classmethod
    def create_hash(cls, msg: str):
        tokens_sorted_by_idf = seq(cls._get_tokens(msg)) \
            .order_by(lambda token: -token.idf) \
            .to_list()

        return IdfHash(
            cls._get_hash(tokens_sorted_by_idf, 1),
            cls._get_hash(tokens_sorted_by_idf, 2),
            cls._get_hash(tokens_sorted_by_idf, 3)
        )

    @classmethod
    def _get_tokens(cls, msg: str) -> List[MsgToken]:
        tokens = []
        for index, word in enumerate(SimpleTokenizer.tokenize(msg)):
            idf = IdfService.get_idf_value(word)
            if idf:
                tokens.append(cls.MsgToken(index, word, idf))
        return tokens

    @classmethod
    def _get_hash(cls, tokens, n):
        return HashFactory.get_hash(
            seq(tokens)
                .take(n)
                .order_by(lambda token: token.index)
                .map(lambda token: token.token)
        )


class IdfHash:
    def __init__(self, hash1, hash2, hash3):
        self.hash1 = hash1
        self.hash2 = hash2
        self.hash3 = hash3
