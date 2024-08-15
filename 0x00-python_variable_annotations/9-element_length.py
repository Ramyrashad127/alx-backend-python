#!/usr/bin/env python3
"""
no modules
"""
from typing import List, Tuple, Sequence, Iterable


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """new function for python"""
    return [(i, len(i)) for i in lst]
