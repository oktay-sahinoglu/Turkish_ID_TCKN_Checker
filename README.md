# Turkish_ID_TCKN_Checker
Extract Turkiye Citizenship Number (TCKN) from text.

## Installation
Just add `src/tckn_checker.py` file to your project.

## Usage
Assuming it is run from the path contains `tckn_checker.py`.

```
>>> from tckn_checker import TCKN_Checker

```
>>> TCKN_Checker.find_tckn("I want to apply and my ID is 12345678950.")
['12345678950']

```

You can perform validation check with or without creating an instance.
```
>>> TCKN_Checker.validate_tckn("12345678950")
True

```
