from typing import *
from .Token import Token

# Computes how many times each word occurs in the list of tokens
class Frequency:
    def __init__(self, tokens: List[Token]):
        self.tokens = tokens
        self.freq_map: Dict[str, int] = {}

    def compute_frequency(self):
        self.freq_map = {}
        for token in self.tokens:
            self.freq_map[token.text] = self.freq_map.get(token.text, 0) + 1

    # Get frequency of a specific word
    def get_frequency(self, word: str) -> int:
        return self.freq_map.get(word.lower(), 0)



