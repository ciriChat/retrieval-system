from .model import IdfPlRepository


class IdfService:
    @staticmethod
    def get_idf_value(word: str):
        return IdfPlRepository.find_idf(word)
