#!/usr/bin/env python3
""" Simple helper function """
import csv
import math
from typing import List, Dict


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


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """ Get the correct page from the dataset
        Args:
            page (int): page number
            page_size (int): size of the page
        Returns:
            List[List]: list of rows of the dataset
        """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0
        start, end = index_range(page, page_size)
        return self.dataset()[start:end]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """ Get the correct page from the dataset
        Args:
            page (int): page number
            page_size (int): size of the page
        Returns:
            Dict: dictionary of pagination
        """
        total_pages = math.ceil(len(self.dataset()) / page_size)
        return {
            "page_size": len(self.get_page(page, page_size)),
            "page": page,
            "data": self.get_page(page, page_size),
            "next_page": page + 1 if page < total_pages else None,
            "prev_page": page - 1 if page > 1 else None,
            "total_pages": total_pages
        }
