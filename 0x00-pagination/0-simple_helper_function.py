#!/usr/bin/env python3
"""helper func"""
from typing import Tuple


def index_range(page, page_size) -> Tuple:
    """func return start and end"""
    return ((page - 1) * page_size, page * page_size)
