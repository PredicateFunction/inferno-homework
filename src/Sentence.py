from src.Error import EmptySentenceError, InvalidWordError
from .Token import Token
from .Frequency import Frequency
from .Tokeniser import Tokeniser
from .Normaliser import Normaliser
from .Parser import Parser
from .Words import Words

from typing import *
import re

# A class which handles the full processing of a sentence
class Sentence:
    def __init__(self, sentence: str):
        self.set_sentence(sentence)

    # Sets a new sentence and processes it
    def set_sentence(self, sentence: str):
        if not sentence.strip():
            raise EmptySentenceError("Cannot set an empty sentence", "Type a valid sentence.")
        self.sentence = sentence
        self.tokens: List[Token] = []
        self.freq_analyser: Frequency = None
        self.process_sentence()

    # Tokenise, normalise, parse, and compute frequencies
    def process_sentence(self):
        tokeniser = Tokeniser(self.sentence)
        raw_tokens = tokeniser.tokenise()
        normaliser = Normaliser(raw_tokens)  # stopwords parameter removed; not used
        normalised_tokens = normaliser.normalise()
        parser = Parser(normalised_tokens)
        self.tokens = parser.parse()
        self.freq_analyser = Frequency(self.tokens)
        self.freq_analyser.compute_frequency()

    # Queries a word: its positions and frequency
    def query_word(self, word: str):
        if not word.strip() or not word.isalpha():
            raise InvalidWordError(f"'{word}' is invalid", "Enter alphabetic words only")

        analyser = Words(self.tokens)
        positions = analyser.find_positions(word)
        frequency = self.freq_analyser.get_frequency(word)

        if positions:
            print("---------------------------")
            print(f"'{word.upper()}' occurs at positions: {positions} (frequency: {frequency})")
            self.display_highlight(word, positions)
        else:
            print(f"'{word.upper()}' does not occur in the sentence.")

    # Prints the sentence highlighting the queried word occurrences
    def display_highlight(self, word: str, positions: List[int]):
        # Remove punctuation for clean display
        words = re.sub(r"[^\w\s]", "", self.sentence).split()
        highlighted = []
        for i, w in enumerate(words, start=1):
            if i in positions:
                highlighted.append(f"\033[92m{w}\033[0m")  # green for matched word
            else:
                highlighted.append(w)
        print(" ".join(highlighted))
        print("---------------------------")
