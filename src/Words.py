from typing import *
from .Token import Token

# Class which finds the positions of a given word in the sentence
class Words:
    def __init__(self, tokens: List[Token]):
        self.tokens = tokens

    # Returns list of positions where the word occurs
    def find_positions(self, word: str) -> List[int]:
        return [token.position for token in self.tokens if token.text.lower() == word.lower()]
