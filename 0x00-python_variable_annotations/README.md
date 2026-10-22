# 0x00. Python - Variable Annotations

## Description
This project focuses on **Python 3 type annotations** and static type analysis using `mypy`:
- Annotating basic types (`str`, `int`, `float`, `bool`).
- Annotating complex collection types using the `typing` module (`List`, `Tuple`, `Dict`, `Set`).
- Defining composite union types (`Union[int, float]`) and optional types (`Optional[Any]`).
- Function signatures accepting or returning callable types (`Callable`).
- Duck typing and verifying type safety using `mypy`.

## Tasks Summary

| File | Description |
| :--- | :--- |
| `0-add.py` | Type-annotated function `add(a: float, b: float) -> float`. |
| `1-concat.py` | Type-annotated function `concat(str1: str, str2: str) -> str`. |
| `2-floor.py` | Type-annotated function `floor(n: float) -> int`. |
| `3-to_str.py` | Type-annotated function `to_str(n: float) -> str`. |
| `5-sum_list.py` | Function taking a list of floats `input_list: List[float]` and returning their sum. |
| `6-sum_mixed_list.py` | Function accepting `mxd_lst: List[Union[int, float]]` and returning sum as float. |
| `7-to_kv.py` | Function taking `k: str` and `v: Union[int, float]` returning tuple of string and squared float. |
| `8-make_multiplier.py` | Function taking `multiplier: float` and returning a callable function `Callable[[float], float]`. |
| `9-element_length.py` | Annotating function parameters with `Iterable` and `Sequence`. |
| `100-safe_first_element.py` | Duck typing annotation for safe first element extraction with `Sequence[Any]` and `Optional[Any]`. |
| `101-safely_get_value.py` | Type variable mapping with `TypeVar('T')` for dictionary value lookup. |
| `102-type_checking.py` | Validating and correcting code to pass strict `mypy` type checking. |

## Verification
```bash
mypy *.py
```

## Author
- **Ramy Rashad** - [GitHub](https://github.com/Ramyrashad127)
