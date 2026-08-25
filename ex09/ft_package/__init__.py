"""Provide list-counting utilities."""


def count_in_list(values: list, target: object) -> int:
    """Return the number of times target occurs in values."""
    return values.count(target)
