import unittest
from mbpp_431_code import common_element

class TestCommonElement(unittest.TestCase):
    def test_common_element_present(self):
        self.assertTrue(common_element([1, 2, 3, 4, 5], [5, 6, 7, 4, 1]))
        self.assertTrue(common_element(['a', 'b', 'c', 'd', 'e'], ['e', 'f', 'g', 'd', 'a']))
        self.assertTrue(common_element([10, 20, 30, 40, 50], [50, 60, 70, 40, 10]))

    def test_common_element_not_present(self):
        self.assertFalse(common_element([1, 2, 3, 4, 5], [6, 7, 8, 9, 0]))
        self.assertFalse(common_element(['a', 'b', 'c', 'd', 'e'], ['f', 'g', 'h', 'i', 'j']))
        self.assertFalse(common_element([10, 20, 30, 40, 50], [0, 0, 0, 0, 0]))

    def test_empty_lists(self):
        self.assertFalse(common_element([], []))
        self.assertFalse(common_element([1], []))
        self.assertFalse(common_element([], [1]))

    def test_single_element_lists(self):
        self.assertTrue(common_element([1], [1]))
        self.assertFalse(common_element([1], [2]))

    def test_lists_with_duplicates(self):
        self.assertTrue(common_element([1, 1, 2, 3, 4], [1, 1, 2, 3, 4]))
        self.assertTrue(common_element(['a', 'a', 'b', 'c', 'd'], ['a', 'a', 'b', 'c', 'd']))
        self.assertTrue(common_element([10, 10, 20, 30, 40], [10, 10, 20, 30, 40]))
