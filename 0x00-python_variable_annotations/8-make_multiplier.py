#!/usr/bin/env python3
"""Module: function
"""

from typing import List, Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Returns a function that multiplies a float by multiplier
    """
    def multiply(x: float) -> float:
        """Multiply x by multiplier
        """
        return x * multiplier
    return multiply
