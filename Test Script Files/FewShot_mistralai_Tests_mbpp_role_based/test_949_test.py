import unittest
from mbpp_949_code import sort_list

class TestSortList(unittest.TestCase):
    def test_sort_ascending(self):
        self.assertEqual(sort_list([1, 10, 2, 3, 4]), "[1, 2, 3, 4, 10]")

    def test_sort_descending(self):
        self.assertEqual(sort_list([10, 9, 8, 7, 6]), "[10, 9, 8, 7, 6]")

    def test_sort_mixed_types(self):
        self.assertEqual(sort_list([1, "a", 3, "b", 2]), "[1, 'a', 2, 'b', 3]")

    def test_sort_empty_list(self):
        self.assertEqual(sort_list([]), "[]")

    def test_sort_single_element(self):
        self.assertEqual(sort_list([1]), "[1]")

    def test_sort_negative_numbers(self):
        self.assertEqual(sort_list([-1, -2, -3]), "[-3, -2, -1]")
