from typing import *
from .Token import Token

# Converts every token lowercase
class Normaliser:
    def __init__(self, tokens: List[Token]):
        self.tokens = tokens

    def normalise(self) -> List[Token]:
        normalised = []
        for token in self.tokens:
            word = token.text.lower()  # convert to lowercase for uniform comparison
            normalised.append(Token(word, token.position))
        return normalised