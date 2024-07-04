#!/usr/bin/env python3
"""Module: Sum of a mixed list
"""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int | float]]) -> float:
    """Returns the sum of the floats in the list
    """
    return sum(mxd_lst)
