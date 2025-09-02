# Represents a single word token in the sentence

class Token:
    def __init__(self, text: str, position: int):
        self.text = text
        self.position = position  # position of the word in the sentence, starting from 1

    def __repr__(self):
        return f"Token(text='{self.text}', position={self.position})"

