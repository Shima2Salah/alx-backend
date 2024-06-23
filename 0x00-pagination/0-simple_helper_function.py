#!/usr/bin/env python3
"""
Main file
"""
from typing import Tuple
def index_range (page, page_size) -> Tuple :
    """func return start and end"""
    return ((page - 1) * page_size, page * page_size)
