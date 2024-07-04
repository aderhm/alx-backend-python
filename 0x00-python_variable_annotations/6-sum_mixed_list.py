#!/usr/bin/env python3
"""Module: Sum of a mixed list
"""

from functools import reduce
from typing import List


def sum_mixed_list(mxd_lst: List[int | float]) -> float:
    """Returns the sum of the floats in the list
    """
    return reduce(lambda x, y: x + y, mxd_lst)
