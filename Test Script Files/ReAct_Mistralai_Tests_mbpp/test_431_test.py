import unittest
from mbpp_431_code import common_element

class TestCommonElement(unittest.TestCase):

    def test_common_element_present(self):
        self.assertTrue(common_element([1, 2, 3, 4, 5], [5, 6, 7, 4, 1]))

    def test_common_element_not_present(self):
        self.assertFalse(common_element([1, 2, 3, 4, 5], [6, 7, 8, 9, 0]))

    def test_empty_lists(self):
        self.assertFalse(common_element([], []))

    def test_single_element_lists(self):
        self.assertFalse(common_element([1], [2]))
        self.assertTrue(common_element([2], [2]))

    def test_one_list_empty(self):
        self.assertFalse(common_element([], [1, 2, 3]))

    def test_duplicate_common_element(self):
        self.assertTrue(common_element([1, 1, 2, 3], [3, 2, 1, 1]))

    def test_case_sensitivity(self):
        self.assertFalse(common_element(['a', 'b', 'c'], ['A', 'B', 'C']))
        self.assertTrue(common_element(['A', 'B', 'C'], ['a', 'b', 'c']))
