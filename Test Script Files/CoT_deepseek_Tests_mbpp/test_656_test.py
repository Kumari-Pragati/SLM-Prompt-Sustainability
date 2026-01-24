import unittest
from mbpp_656_code import find_Min_Sum

class TestFindMinSum(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(find_Min_Sum([1, 2, 3], [4, 5, 6], 3), 9)

    def test_typical_case_with_duplicates(self):
        self.assertEqual(find_Min_Sum([1, 2, 2], [4, 5, 6], 3), 7)

    def test_empty_lists(self):
        self.assertEqual(find_Min_Sum([], [], 0), 0)

    def test_single_element_lists(self):
        self.assertEqual(find_Min_Sum([1], [2], 1), 1)

    def test_negative_numbers(self):
        self.assertEqual(find_Min_Sum([-1, -2, -3], [-4, -5, -6], 3), 9)

    def test_large_numbers(self):
        self.assertEqual(find_Min_Sum([100, 200, 300], [400, 500, 600], 3), 900)

    def test_invalid_input_type(self):
        with self.assertRaises(TypeError):
            find_Min_Sum("1, 2, 3", [4, 5, 6], 3)

    def test_invalid_input_length(self):
        with self.assertRaises(ValueError):
            find_Min_Sum([1, 2, 3], [4, 5, 6, 7], 3)
