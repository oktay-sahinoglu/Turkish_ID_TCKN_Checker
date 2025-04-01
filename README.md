# Turkish_ID_TCKN_Checker
Extract Turkiye Citizenship Number (TCKN) from text.

## Installation
Just add `src/tckn_checker.py` file to your project.

## Usage
Assuming it is run from the path contains `tckn_checker.py`.

```
>>> from tckn_checker import TCKN_Checker

```

```
>>> TCKN_Checker.find_tckn("I want to apply and my ID is 12345678950.")
['12345678950']

```

Let's change one digit to make ID number invalid.

```
>>> TCKN_Checker.find_tckn("I want to apply and my ID is 12345678955.")
[]

```

You can also perform validation check.
```
>>> TCKN_Checker.validate_tckn("12345678950")
True

>>> TCKN_Checker.validate_tckn("12345678955")
False

```
