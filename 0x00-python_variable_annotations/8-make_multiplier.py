#!/usr/bin/env python3
"""
no modules
"""
from typing import Callable

def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """new function for python"""
    def multiply_by_multiplier(value: float) -> float:
        """new function for python"""
        return value * multiplier

    return multiply_by_multiplier
