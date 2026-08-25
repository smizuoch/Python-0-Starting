import sys


def encode_morse(text: str) -> str:
    """Return an ASCII alphanumeric string encoded as Morse code."""
    nested_morse = {
        " ": "/",
        "A": ".-",
        "B": "-...",
        "C": "-.-.",
        "D": "-..",
        "E": ".",
        "F": "..-.",
        "G": "--.",
        "H": "....",
        "I": "..",
        "J": ".---",
        "K": "-.-",
        "L": ".-..",
        "M": "--",
        "N": "-.",
        "O": "---",
        "P": ".--.",
        "Q": "--.-",
        "R": ".-.",
        "S": "...",
        "T": "-",
        "U": "..-",
        "V": "...-",
        "W": ".--",
        "X": "-..-",
        "Y": "-.--",
        "Z": "--..",
        "0": "-----",
        "1": ".----",
        "2": "..---",
        "3": "...--",
        "4": "....-",
        "5": ".....",
        "6": "-....",
        "7": "--...",
        "8": "---..",
        "9": "----.",
    }
    assert isinstance(text, str), "the arguments are bad"
    characters = text.upper()
    assert all(character in nested_morse for character in characters), (
        "the arguments are bad"
    )
    return " ".join(nested_morse[character] for character in characters)


def main() -> None:
    """Encode one command-line argument as Morse code."""
    try:
        assert len(sys.argv) == 2, "the arguments are bad"
        print(encode_morse(sys.argv[1]))
    except AssertionError:
        print("AssertionError: the arguments are bad")


if __name__ == "__main__":
    main()
