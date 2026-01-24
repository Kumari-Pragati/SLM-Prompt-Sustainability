import unittest
from mbpp_265_code import list_split

class TestListSplit(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(list_split([], 2), [[]])

    def test_single_element_list(self):
        self.assertEqual(list_split([1], 2), [[1]])

    def test_multiple_elements_list(self):
        self.assertEqual(list_split([1, 2, 3, 4, 5], 2), [[1, 2], [3, 4], [5]])

    def test_step_greater_than_list_length(self):
        self.assertEqual(list_split([1, 2, 3, 4, 5], 10), [[1, 2, 3, 4, 5]])

    def test_step_equal_to_list_length(self):
        self.assertEqual(list_split([1, 2, 3, 4, 5], 5), [[1], [2], [3], [4], [5]])

    def test_step_less_than_list_length(self):
        self.assertEqual(list_split([1, 2, 3, 4, 5], 1), [[1, 2, 3, 4, 5]])
