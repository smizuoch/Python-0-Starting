import os


def ft_tqdm(lst: range) -> None:
    """Yield each range element while displaying a progress bar."""
    total = len(lst)
    if total == 0:
        return

    try:
        terminal_width = os.get_terminal_size().columns
    except OSError:
        terminal_width = 80

    total_width = len(str(total))
    for current, element in enumerate(lst, start=1):
        yield element
        percentage = int(current / total * 100)
        counter = f"{current:>{total_width}}/{total}"
        prefix = f"{percentage:3d}%|["
        suffix = f"]| {counter}"
        bar_width = max(1, terminal_width - len(prefix) - len(suffix))
        completed = max(1, int(bar_width * current / total))
        bar = (
            "=" * (completed - 1)
            + ">"
            + " " * (bar_width - completed)
        )
        print(f"\r{prefix}{bar}{suffix}", end="", flush=True)


def main() -> None:
    """Provide no standalone behavior for this importable module."""
    pass


if __name__ == "__main__":
    main()
