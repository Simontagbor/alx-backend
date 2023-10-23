#!/usr/bin/env python3
""" Simple helper function """


def index_range(page, page_size):
    """ Return a tuple of size two containing a
    start index and an end index corresponding
    
    Args:
        page (int): page number
        page_size (int): size of the page
    
    Returns:
        tuple: start index and end index
    """
    start_index = (page - 1) * page_size
    end_index = page * page_size
    return (start_index, end_index)
