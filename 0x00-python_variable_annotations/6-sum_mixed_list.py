#!/usr/bin/env python3
"""
no modules
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """sum elements int/float"""
    su: float = 0.0
    for i in mxd_lst:
        su += i
    return su
