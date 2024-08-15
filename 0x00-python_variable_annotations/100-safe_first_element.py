#!/usr/bin/env python3
"""import modules"""
from typing import Any, Sequence, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """new function for python"""
    if lst:
        return lst[0]
    else:
        return None
