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
        self.assertFalse(common_element([1], []))
        self.assertFalse(common_element([], [1]))

    def test_one_list_contains_none(self):
        self.assertFalse(common_element([1, None], [2, 3]))
