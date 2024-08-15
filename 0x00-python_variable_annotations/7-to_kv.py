#!/usr/bin/env python3
"""
no modules
"""
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[int, float]:
    """sum"""
    return (k, float(v ** 2))