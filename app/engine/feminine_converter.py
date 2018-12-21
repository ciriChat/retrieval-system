from functional import seq

from app.engine.message import Message
from app.morph.model import MorphRepository
from app.morph.service import MorphTokenFactory, MorphToken, MorphTags


class MessageToFeminineFormConverter:
    @classmethod
    def convert(cls, msg: Message) -> Message:
        new_morph_tokens = []
        new_tokens = []
        replaced = False
        for token in msg.morph_tokens:
            if cls._can_replace(token):
                feminine_tag = cls._get_feminine_tags(token.tags)
                morph_record = MorphRepository.find_word_by_tags(token.base_form, feminine_tag)
                if morph_record:
                    replaced = True
                    new_morph_tokens.append(MorphTokenFactory.from_morph_record(token.token, morph_record))
                else:
                    new_morph_tokens.append(token)
            else:
                new_morph_tokens.append(token)

        if not replaced:
            return msg

        text = ' '.join(seq(new_morph_tokens).map(lambda t: t.token))
        return Message(text, msg.tokens, new_tokens)

    @staticmethod
    def _can_replace(token: MorphToken) -> bool:
        tags: MorphTags = token.tags
        if not tags:
            return False

        return tags.is_verb() \
            and tags.is_singular() \
            and tags.is_first_person() \
            and tags.is_masculine() \
            and not tags.is_feminine()

    @classmethod
    def _get_feminine_tags(cls, tags: MorphTags) -> str:
        groups = tags.get_tags()
        for index, group in enumerate(groups):
            if 'm1' in group or 'm2' in group or 'm3' in group:
                groups[index] = 'f'
        return tags.TAG_SEPARATOR.join(groups)