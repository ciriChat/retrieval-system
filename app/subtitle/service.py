from typing import List
from functional import seq

from .model import SubtitleRepository
from .hasher import IdfHashFactory


class SubtitleService:
    @staticmethod
    def find_similar_subs_by_idf(msg: str) -> List[str]:
        idf_hash = IdfHashFactory.create_hash(msg)

        subs = seq(SubtitleRepository.find_by_hash3(idf_hash.hash3))
        if not subs:
            subs = seq(SubtitleRepository.find_by_hash2(idf_hash.hash2))
        if not subs:
            subs = seq(SubtitleRepository.find_by_hash1(idf_hash.hash1))
        return subs.map(lambda sub: sub.text).to_list()

    @staticmethod
    def find_next_subs_by_idf(msg: str) -> List[str]:
        idf_hash = IdfHashFactory.create_hash(msg)

        subs = seq(SubtitleRepository.find_next_by_hash3(idf_hash.hash3))
        if not subs:
            subs = seq(SubtitleRepository.find_next_by_hash2(idf_hash.hash2))
        if not subs:
            subs = seq(SubtitleRepository.find_next_by_hash1(idf_hash.hash1))
        return subs.map(lambda sub: sub.text).to_list()
