from src.Sentence import Sentence
from src.Error import AnalyserError
import sys


# Program execution
if __name__ == "__main__":
    sentence = (
        "DO NOT JUDGE ME BY MY SUCCESSES "
        "JUDGE ME BY HOW MANY TIMES I FELL DOWN AND GOT BACK UP AGAIN"
    )

    system = Sentence(sentence)

    print("Type '!!exit' to quit.\n")
    print("Type '!!set' to set a new sentence.\n")

    try:
        while True:
            print(f"Sentence: {system.sentence}")
            target = input("Enter a word to find: ").strip()
            if target.lower() == "!!exit":
                print("Exiting")
                break
            elif target.lower().startswith("!!set"):
                # Get the new sentence after the command
                new_sentence = target[6:].strip()  # len("!!set ") = 6
                if not new_sentence:
                    print("\033[91mError: Sentence cannot be empty\033[0m\n")
                    continue
                system = Sentence(new_sentence)
                print("\033[92mNew sentence set successfully!\033[0m\n")
                continue

            try:
                system.query_word(target)
            except AnalyserError:
                pass  # error already displayed with red text
            print()  # spacing between queries
    except KeyboardInterrupt:
        sys.exit(0)
