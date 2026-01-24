import unittest
from mbpp_106_code import List, Tuple

from 106_code import add_lists

class TestAddLists(unittest.TestCase):

    def test_empty_list_and_tuple(self):
        self.assertListEqual(add_lists([], (1, 2, 3)), [1, 2, 3])

    def test_list_and_empty_tuple(self):
        self.assertListEqual(add_lists([1, 2, 3], []), [1, 2, 3])

    def test_list_and_tuple(self):
        self.assertListEqual(add_lists([1, 2, 3], (4, 5, 6)), [1, 2, 3, 4, 5, 6])

    def test_list_with_duplicates_and_tuple(self):
        self.assertListEqual(add_lists([1, 2, 2, 3], (4, 5, 6)), [1, 2, 2, 3, 4, 5, 6])

    def test_tuple_with_duplicates_and_list(self):
        self.assertListEqual(add_lists([1, 2, 3], (4, 4, 5, 6)), [1, 2, 3, 4, 4, 5, 6])
