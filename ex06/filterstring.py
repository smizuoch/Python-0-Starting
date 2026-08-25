import sys

from ft_filter import ft_filter


def main() -> None:
    """Print words longer than the integer given on the command line."""
    try:
        assert len(sys.argv) == 3, "the arguments are bad"
        text = sys.argv[1]
        minimum_length = int(sys.argv[2])
        words = text.split()
        result = ft_filter(
            lambda word: len(word) > minimum_length,
            words,
        )
        print(result)
    except (AssertionError, ValueError):
        print("AssertionError: the arguments are bad")


if __name__ == "__main__":
    main()
