from ft_package import count_in_list


def main() -> None:
    """Test counting present, missing, and non-string values."""
    assert count_in_list(["toto", "tata", "toto"], "toto") == 2
    assert count_in_list(["toto", "tata", "toto"], "tutu") == 0
    assert count_in_list([1, 2, 1, 1], 1) == 3
    print("All tests passed.")


if __name__ == "__main__":
    main()
