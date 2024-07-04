#!/usr/bin/env python3
"""Module: string and int/float to tuple
"""

from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Returns a tuple of strings and ints/floats
    """
    return (k, v**2)
