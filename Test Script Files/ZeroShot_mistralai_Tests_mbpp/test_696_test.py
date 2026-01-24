import unittest
from mbpp_696_code import zip_longest as zip
from six.moves import map
from typing import List

def zip_list(list1: List[int], list2: List[int]) -> List[int]:
    result = list(map(lambda x, y: x + y, list1, list2))
    return result

class TestZipList(unittest.TestCase):

    def test_empty_lists(self):
        self.assertListEqual(zip_list([], []), [])

    def test_single_element_lists(self):
        self.assertListEqual(zip_list([1], []), [1])
        self.assertListEqual(zip_list([], [2]), [2])

    def test_lists_of_same_length(self):
        self.assertListEqual(zip_list([1, 2, 3], [4, 5, 6]), [5, 7, 9])

    def test_lists_of_different_lengths(self):
        self.assertListEqual(zip_list([1, 2, 3], [4, 5]), [5, 7, None])
        self.assertListEqual(zip_list([1, 2, 3], [4]), [4, 6, 7])
