# base exception class
class AnalyserError(Exception):
    def __init__(self, message: str, suggestion: str = ""):
        super().__init__(message)
        self.suggestion = suggestion
        # Print message in red automatically
        print(f"\033[91mError: {message}\033[0m")
        if suggestion:
            print(f"\033[93mSuggestion: {suggestion}\033[0m")
        # Log to file 
        with open("analyser_errors.log", "a") as f:
            f.write(f"Error: {message}\n")
            if suggestion:
                f.write(f"Suggestion: {suggestion}\n")


# raised when the input sentence is empty
class EmptySentenceError(AnalyserError):
    def __init__(self, message: str = "The sentence is empty", suggestion: str = "Provide a valid sentence with words"):
        super().__init__(message, suggestion)

# raised when the user enters an invalid word
class InvalidWordError(AnalyserError):
    def __init__(self, message: str = "Invalid word entered", suggestion: str = "Enter alphabetic words only"):
        super().__init__(message, suggestion)