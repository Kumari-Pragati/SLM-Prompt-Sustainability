import unittest
from mbpp_42_code import find_Sum

class TestFindSum(unittest.TestCase):

    def test_single_element(self):
        self.assertEqual(find_Sum([1], 1), 1)

    def test_no_duplicates(self):
        self.assertEqual(find_Sum([1, 2, 3], 3), 6)

    def test_duplicates(self):
        self.assertEqual(find_Sum([1, 2, 2, 3, 4, 4], 6), 6)

    def test_empty_list(self):
        with self.assertRaises(TypeError):
            find_Sum([], 1)

    def test_non_integer_input(self):
        with self.assertRaises(TypeError):
            find_Sum([1, 2, 3], 'a')

    def test_non_list_input(self):
        with self.assertRaises(TypeError):
            find_Sum('abc', 1)
