from typing import *
from .Token import Token

# Parser class, currently just returns the tokens as-is
class Parser:
    def __init__(self, tokens: List[Token]):
        self.tokens = tokens

    def parse(self) -> List[Token]:
        return self.tokens
