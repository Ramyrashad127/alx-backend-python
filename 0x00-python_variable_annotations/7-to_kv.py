#!/usr/bin/env python3
"""
no modules
"""
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """sum"""
    x = v ** 2
    return (k, x)
