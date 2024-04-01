#!/usr/bin/env python3
"""Contains a definition of index_page function."""

from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Takes two integer arguments and returns a turple
    of sixe containing start index and end index
    """
    start, end = 0, 0
    for i in range(page):
        start = end
        end += page_size

    return (start, end)
