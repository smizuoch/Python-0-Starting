import subprocess
import sys
from pathlib import Path

from sos import encode_morse


def run_sos(arguments: list[str]) -> str:
    """Run sos.py and return its standard output."""
    script = Path(__file__).with_name("sos.py")
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
    """Test letters, digits, spaces, and invalid arguments."""
    assert encode_morse("sos") == "... --- ..."
    assert encode_morse("42 Tokyo") == (
        "....- ..--- / - --- -.- -.-- ---"
    )

    assert run_sos(["sos"]) == "... --- ...\n"
    assert run_sos(["42 Tokyo"]) == (
        "....- ..--- / - --- -.- -.-- ---\n"
    )

    expected_error = "AssertionError: the arguments are bad\n"
    assert run_sos(["h$llo"]) == expected_error
    assert run_sos([]) == expected_error
    assert run_sos(["sos", "extra"]) == expected_error
    print("All tests passed.")


if __name__ == "__main__":
    main()
