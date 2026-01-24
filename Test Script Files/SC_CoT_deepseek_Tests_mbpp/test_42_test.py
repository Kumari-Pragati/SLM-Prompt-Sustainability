import unittest
from mbpp_42_code import find_Sum

class TestFindSum(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(find_Sum([1, 2, 3, 2, 1], 5), 4)

    def test_edge_case_empty_array(self):
        self.assertEqual(find_Sum([], 0), 0)

    def test_edge_case_single_element(self):
        self.assertEqual(find_Sum([1], 1), 0)

    def test_edge_case_all_same_elements(self):
        self.assertEqual(find_Sum([1, 1, 1, 1, 1], 5), 5)

    def test_corner_case_negative_numbers(self):
        self.assertEqual(find_Sum([-1, -2, -3, -2, -1], 5), -4)

    def test_corner_case_mixed_numbers(self):
        self.assertEqual(find_Sum([-1, 2, -3, 2, -1], 5), 0)

    def test_invalid_input_non_integer_elements(self):
        with self.assertRaises(TypeError):
            find_Sum(['1', 2, 3, 2, '1'], 5)

    def test_invalid_input_negative_length(self):
        with self.assertRaises(ValueError):
            find_Sum([1, 2, 3, 2, 1], -1)
