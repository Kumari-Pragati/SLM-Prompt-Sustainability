import unittest
from mbpp_869_code import remove_list_range

class TestRemoveListRange(unittest.TestCase):

    def test_empty_list(self):
        self.assertListEqual(remove_list_range([], 1, 1), [])

    def test_single_element_list(self):
        self.assertListEqual(remove_list_range([1], 1, 1), [])
        self.assertListEqual(remove_list_range([1], 0, 1), [])
        self.assertListEqual(remove_list_range([1], 1, 2), [1])

    def test_list_with_single_range_element(self):
        self.assertListEqual(remove_list_range([1, 2], 1, 2), [2])
        self.assertListEqual(remove_list_range([1, 2], 0, 1), [1])

    def test_list_with_multiple_range_elements(self):
        self.assertListEqual(remove_list_range([1, 2, 3, 4, 5], 2, 4), [2, 3, 4])
        self.assertListEqual(remove_list_range([1, 2, 3, 4, 5], 1, 5), [1, 2, 3, 4, 5])
        self.assertListEqual(remove_list_range([1, 2, 3, 4, 5], 0, 6), [])
        self.assertListEqual(remove_list_range([1, 2, 3, 4, 5], -1, 5), [])
        self.assertListEqual(remove_list_range([1, 2, 3, 4, 5], 6, 6), [])

    def test_list_with_min_greater_than_max(self):
        self.assertListEqual(remove_list_range([[1, 2], [3, 4]], 2, 1), [])

    def test_list_with_non_iterable_elements(self):
        self.assertRaises(TypeError, remove_list_range, [1, 2, 3], 'a', 'b')
