import unittest
from mbpp_949_code import sort_list

class TestSortList(unittest.TestCase):

    def test_simple_list(self):
        self.assertEqual(sort_list([1, 10, 2, 20]), "'[1, 2, 10, 20]'")

    def test_list_with_duplicates(self):
        self.assertEqual(sort_list([1, 1, 10, 10, 2, 20]), "'[1, 1, 2, 10, 10, 20]'")

    def test_empty_list(self):
        self.assertEqual(sort_list([]), "'[]'")

    def test_list_with_only_zero(self):
        self.assertEqual(sort_list([0]), "'[0]'")

    def test_list_with_only_negative_numbers(self):
        self.assertEqual(sort_list([-1, -10, -2, -20]), "'[-20, -10, -2, -1]'")

    def test_list_with_large_numbers(self):
        self.assertEqual(sort_list([1000000, 100000, 10000, 1000]), "'[1000, 10000, 100000, 1000000]'")

    def test_list_with_mixed_types(self):
        self.assertEqual(sort_list([1, 'a', 10, 2.5]), "'[1, 10, 2.5, 'a']'")
