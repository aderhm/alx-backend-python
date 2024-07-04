#!/usr/bin/env python3
"""Module: Sum of a list of floats
"""

from functools import reduce
from typing import List


def sum_list(input_list: List) -> float:
    """Returns the sum of the floats in the list
    """
    return reduce(lambda x, y: x + y, input_list)
