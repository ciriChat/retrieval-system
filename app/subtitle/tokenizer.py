import re
from typing import List


class SimpleTokenizer:
    NON_ALPHA_REGEX = re.compile('[^A-Za-zżźćńółęąśŻŹĆĄŚĘŁÓŃ ]+')

    @classmethod
    def tokenize(cls, text: str) -> List[str]:
        return cls.get_words(cls.remove_non_word_chars(text))

    @classmethod
    def raw_tokenize(cls, text: str) -> List[str]:
        return text.split()

    @classmethod
    def remove_non_word_chars(cls, text: str):
        return cls.NON_ALPHA_REGEX.sub('', text).strip()

    @staticmethod
    def get_words(text: str):
        return text.lower().split()
