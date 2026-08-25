# ft_package

`ft_package` is a small example Python package created for Exercise 09 of the 42 Python for Data Science piscine.

## Build

Run the following command from the `ex09` directory:

```sh
python -m build
```

## Installation

Install either generated distribution:

```sh
pip install ./dist/ft_package-0.0.1.tar.gz
pip install ./dist/ft_package-0.0.1-py3-none-any.whl
```

## Usage

```python
from ft_package import count_in_list

print(count_in_list(["toto", "tata", "toto"], "toto"))
print(count_in_list(["toto", "tata", "toto"], "tutu"))
```

The output is:

```text
2
0
```
