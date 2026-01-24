import unittest
from mbpp_777_code import find_Sum

class TestFindSum(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(find_Sum([], 0), 0)

    def test_single_element_list(self):
        self.assertEqual(find_Sum([1], 1), 1)

    def test_consecutive_elements(self):
        self.assertEqual(find_Sum([1, 2, 3, 4, 5], 5), 15)

    def test_non_consecutive_elements(self):
        self.assertEqual(find_Sum([1, 2, 3, 4, 2, 5], 6), 15)

    def test_duplicate_elements(self):
        self.assertEqual(find_Sum([1, 1, 2, 3, 4, 5], 6), 15)

    def test_negative_numbers(self):
        self.assertEqual(find_Sum([-1, -2, -3, -4, -5], 5), -15)

    def test_zero(self):
        self.assertEqual(find_Sum([0], 1), 0)
        self.assertEqual(find_Sum([0, 0], 2), 0)

    def test_invalid_input_list(self):
        self.assertRaises(TypeError, find_Sum, 'list', 0)

    def test_invalid_input_n(self):
        self.assertRaises(TypeError, find_Sum, [1, 2, 3], 'int')
