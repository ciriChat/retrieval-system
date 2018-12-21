from app.morph.service import MorphService, MorphTags, MorphToken
from app.subtitle.tokenizer import SimpleTokenizer
from typing import List


class Message:
    def __init__(self, text, tokens, morph_tokens: List[MorphToken]):
        self.text = text
        self.tokens = tokens
        self.morph_tokens = morph_tokens


class MessageFactory:
    @staticmethod
    def from_text_msg(text: str) -> Message:
        tokens = SimpleTokenizer.tokenize(text)
        morph_tokens = MorphService.get_morph_tokens(text.split())
        return Message(text, tokens, morph_tokens)
