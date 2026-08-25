import io
from contextlib import redirect_stdout

from Loading import ft_tqdm


def main() -> None:
    """Test yielded elements and the final progress display."""
    output = io.StringIO()
    with redirect_stdout(output):
        yielded_elements = [element for element in ft_tqdm(range(3))]

    progress = output.getvalue()
    assert yielded_elements == [0, 1, 2]
    assert progress.count("\r") == 3
    assert "100%|[" in progress
    assert progress.endswith("]| 3/3")

    empty_output = io.StringIO()
    with redirect_stdout(empty_output):
        assert list(ft_tqdm(range(0))) == []
    assert empty_output.getvalue() == ""
    print("All tests passed.")


if __name__ == "__main__":
    main()
