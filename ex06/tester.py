import subprocess
import sys
from pathlib import Path

from ft_filter import ft_filter


def run_filterstring(arguments: list[str]) -> str:
    """Run filterstring.py and return its standard output."""
    script = Path(__file__).with_name("filterstring.py")
    result = subprocess.run(
        [sys.executable, str(script), *arguments],
        capture_output=True,
        text=True,
        check=False,
    )
    assert result.returncode == 0
    assert result.stderr == ""
    return result.stdout


def main() -> None:
    """Test ft_filter and the required filterstring cases."""
    assert ft_filter(lambda number: number % 2 == 0, range(6)) == [0, 2, 4]
    assert ft_filter(None, [0, 1, "", "Python", False]) == [1, "Python"]
    assert ft_filter.__doc__ == filter.__doc__

    assert run_filterstring(["Hello the World ", "4"]) == (
        "['Hello', 'World']\n"
    )
    assert run_filterstring(["Hello the World ", "99"]) == "[]\n"

    expected_error = "AssertionError: the arguments are bad\n"
    assert run_filterstring(["3", "Hello the World "]) == expected_error
    assert run_filterstring([]) == expected_error
    assert run_filterstring(["one", "2", "extra"]) == expected_error
    print("All tests passed.")


if __name__ == "__main__":
    main()
