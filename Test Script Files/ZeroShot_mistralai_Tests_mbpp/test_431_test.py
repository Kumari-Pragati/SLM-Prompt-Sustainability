import unittest
from mbpp_431_code import common_element

class TestCommonElement(unittest.TestCase):
    def test_empty_lists(self):
        self.assertFalse(common_element([], []))

    def test_single_element_lists(self):
        self.assertTrue(common_element([1], [1]))
        self.assertFalse(common_element([1], [2]))

    def test_lists_with_duplicates(self):
        self.assertTrue(common_element([1, 1, 2], [2, 1, 3]))

    def test_lists_with_multiple_common_elements(self):
        self.assertTrue(common_element([1, 2, 3], [3, 2, 1]))

    def test_lists_with_no_common_elements(self):
        self.assertFalse(common_element([1, 2, 3], [4, 5, 6]))
