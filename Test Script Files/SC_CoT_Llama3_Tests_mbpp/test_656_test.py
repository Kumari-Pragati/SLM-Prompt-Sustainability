import unittest
from mbpp_656_code import find_Min_Sum

class TestFindMinSum(unittest.TestCase):
    def test_typical_inputs(self):
        self.assertEqual(find_Min_Sum([1, 2, 3], [4, 5, 6], 3), 9)

    def test_edge_case_equal_lists(self):
        self.assertEqual(find_Min_Sum([1, 1, 1], [1, 1, 1], 3), 0)

    def test_edge_case_empty_lists(self):
        self.assertEqual(find_Min_Sum([], [], 0), 0)

    def test_edge_case_single_element_lists(self):
        self.assertEqual(find_Min_Sum([1], [1], 1), 0)

    def test_edge_case_negative_numbers(self):
        self.assertEqual(find_Min_Sum([-1, -2, -3], [1, 2, 3], 3), 12)

    def test_edge_case_zero_sum(self):
        self.assertEqual(find_Min_Sum([1, 2, 3], [3, 2, 1], 3), 0)

    def test_invalid_input_type(self):
        with self.assertRaises(TypeError):
            find_Min_Sum('a', [1, 2, 3], 3)

    def test_invalid_input_length(self):
        with self.assertRaises(IndexError):
            find_Min_Sum([1, 2], [1, 2, 3, 4], 2)
