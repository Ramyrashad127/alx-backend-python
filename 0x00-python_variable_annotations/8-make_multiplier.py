#!/usr/bin/env python3
"""
no modules
"""
from typing import Callable

def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """function"""
    def multiply_by_multiplier(value: float) -> float:
        """function"""
        return value * multiplier

    return multiply_by_multiplier
