#!/usr/bin/env python3
"""import modules"""
from typing import List, Tuple


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """new function for python"""
    arr: List = [
        item for item in lst
        for i in range(int(factor))
    ]
    return arr


array = (12, 72, 91)

x2 = zoom_array(array)

x3 = zoom_array(array, 3)
