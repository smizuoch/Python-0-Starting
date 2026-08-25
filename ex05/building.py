import string
import sys


def display_character_counts(text: str) -> None:
    """Display the character categories contained in text."""
    upper_letters = sum(character.isupper() for character in text)
    lower_letters = sum(character.islower() for character in text)
    punctuation_marks = sum(
        character in string.punctuation for character in text
    )
    spaces = sum(character.isspace() for character in text)
    digits = sum(character.isdigit() for character in text)

    print(f"The text contains {len(text)} characters:")
    print(f"{upper_letters} upper letters")
    print(f"{lower_letters} lower letters")
    print(f"{punctuation_marks} punctuation marks")
    print(f"{spaces} spaces")
    print(f"{digits} digits")


def main() -> None:
    """Read one text argument and display its character counts."""
    try:
        assert len(sys.argv) <= 2, "more than one argument is provided"
        if len(sys.argv) == 1 or sys.argv[1] == "":
            print("What is the text to count?")
            text = sys.stdin.read()
        else:
            text = sys.argv[1]
        display_character_counts(text)
    except AssertionError as error:
        print(f"AssertionError: {error}")


if __name__ == "__main__":
    main()
