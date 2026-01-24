import unittest
from mbpp_656_code import find_Min_Sum

class TestFindMinSum(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(find_Min_Sum([1, 2, 3], [4, 5, 6], 3), 9)

    def test_empty_lists(self):
        self.assertEqual(find_Min_Sum([], [], 0), 0)

    def test_single_element_lists(self):
        self.assertEqual(find_Min_Sum([1], [2], 1), 1)

    def test_negative_numbers(self):
        self.assertEqual(find_Min_Sum([-1, -2, -3], [-4, -5, -6], 3), 15)

    def test_large_numbers(self):
        self.assertEqual(find_Min_Sum([1000, 2000, 3000], [4000, 5000, 6000], 3), 15000)

    def test_equal_elements(self):
        self.assertEqual(find_Min_Sum([1, 2, 3], [1, 2, 3], 3), 0)

    def test_unequal_length_lists(self):
        with self.assertRaises(IndexError):
            find_Min_Sum([1, 2, 3], [4, 5], 3)
