import unittest
from mbpp_42_code import find_Sum

class TestFindSum(unittest.TestCase):
    def test_single_element(self):
        self.assertEqual(find_Sum([1], 1), 0)
        self.assertEqual(find_Sum([2], 2), 0)

    def test_two_elements(self):
        self.assertEqual(find_Sum([1, 1], 2), 1)
        self.assertEqual(find_Sum([2, 2], 2), 4)

    def test_multiple_elements(self):
        self.assertEqual(find_Sum([1, 1, 2, 2], 4), 2)
        self.assertEqual(find_Sum([1, 1, 2, 3, 3], 4), 2)

    def test_empty_list(self):
        self.assertEqual(find_Sum([], 0), 0)

    def test_negative_numbers(self):
        self.assertEqual(find_Sum([-1, -1, 0, 2], 3), -1)

    def test_large_numbers(self):
        self.assertEqual(find_Sum([1000, 1000, 2000], 3), 1000)

    def test_invalid_input(self):
        self.assertRaises(TypeError, find_Sum, [1, 2], 'n')
        self.assertRaises(TypeError, find_Sum, [1, 2], 1.5)
