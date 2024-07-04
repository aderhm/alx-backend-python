#!/usr/bin/env python3
"""Module: Duck type the first element of a sequence
"""

from typing import Any, Sequence, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """Returns the first element of list
    """
    if lst:
        return lst[0]
    else:
        return None
