import unittest
from mbpp_431_code import common_element

class TestCommonElement(unittest.TestCase):

    def test_common_element_present(self):
        self.assertTrue(common_element([1, 2, 3, 4, 5], [5, 6, 7, 5, 8]))
        self.assertTrue(common_element(["apple", "banana", "cherry"], ["cherry", "date", "apple"]))
        self.assertTrue(common_element([1.1, 2.2, 3.3, 4.4, 5.5], [5.5, 6.6, 7.7, 5.5, 8.8]))

    def test_no_common_element(self):
        self.assertFalse(common_element([1, 2, 3, 4, 5], [6, 7, 8, 9, 10]))
        self.assertFalse(common_element(["apple", "banana", "cherry"], ["date", "orange", "grape"]))
        self.assertFalse(common_element([1.1, 2.2, 3.3, 4.4, 5.5], [6.6, 7.7, 8.8, 9.9, 10.10]))

    def test_empty_lists(self):
        self.assertFalse(common_element([], []))
        self.assertFalse(common_element([1], []))
        self.assertFalse(common_element([], [1]))

    def test_single_element_lists(self):
        self.assertTrue(common_element([1], [1]))
        self.assertFalse(common_element([1], [2]))

    def test_lists_with_duplicates(self):
        self.assertTrue(common_element([1, 1, 2, 3], [1, 2, 3, 1]))
        self.assertTrue(common_element(["apple", "apple", "banana"], ["apple", "banana", "apple"]))
        self.assertTrue(common_element([1.1, 1.1, 2.2, 3.3], [1.1, 2.2, 3.3, 1.1]))
