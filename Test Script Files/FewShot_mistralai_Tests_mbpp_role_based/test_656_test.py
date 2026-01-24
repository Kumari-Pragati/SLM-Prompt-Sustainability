import unittest
from mbpp_656_code import find_Min_Sum

class TestFindMinSum(unittest.TestCase):
    def test_positive_numbers(self):
        a = [1, 2, 3, 4]
        b = [1, 2, 3, 4]
        self.assertEqual(find_Min_Sum(a, b, len(a)), 0)

    def test_different_lengths(self):
        a = [1, 2, 3]
        b = [1, 2, 3, 4]
        self.assertEqual(find_Min_Sum(a, b, len(a)), 4)

    def test_negative_numbers(self):
        a = [-1, -2, -3]
        b = [-1, -2, -3]
        self.assertEqual(find_Min_Sum(a, b, len(a)), 0)

    def test_empty_lists(self):
        a = []
        b = []
        self.assertEqual(find_Min_Sum(a, b, len(a)), 0)

    def test_single_element_lists(self):
        a = [1]
        b = [1]
        self.assertEqual(find_Min_Sum(a, b, len(a)), 0)

    def test_negative_and_positive_numbers(self):
        a = [-1, 1]
        b = [-1, 1]
        self.assertEqual(find_Min_Sum(a, b, len(a)), 0)

    def test_invalid_input_length(self):
        a = [1, 2, 3]
        b = [1, 2, 3]
        with self.assertRaises(IndexError):
            find_Min_Sum(a, b, len(a) + 1)
