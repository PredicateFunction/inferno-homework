from typing import *
from .Token import Token
from .Error import EmptySentenceError

# Set of punctuation characters to consider during tokenisation
PUNCTUATION = {".", ",", "!", "?", ";", ":", "(", ")", "[", "]", "{", "}", '"', "'"}  # extendable if needed

# Builds tokens from the given sentence
class Tokeniser:

    def __init__(self, sentence: str):
        self.sentence = sentence

    def tokenise(self) -> List[Token]:
        if not self.sentence.strip():
            raise EmptySentenceError("The sentence is empty", "Provide a valid sentence with words")

        tokens = []
        word = ""
        position = 1  # first word position starts at 1

        # iterate through each character in the sentence
        for char in self.sentence:
            if char.isspace() or char in PUNCTUATION:
                # end of a word detected
                if word:
                    tokens.append(Token(word, position))
                    position += 1
                    word = ""
            else:
                # keep building the current word
                word += char  

        # append the last word if sentence doesn't end with punctuation
        if word:
            tokens.append(Token(word, position))

        return tokens
