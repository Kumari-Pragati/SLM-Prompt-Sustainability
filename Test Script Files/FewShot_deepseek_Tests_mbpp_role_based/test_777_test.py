import unittest
from mbpp_777_code import find_Sum

class TestFindSum(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(find_Sum([1, 2, 3, 4, 5], 5), 15)

    def test_edge_case_single_element(self):
        self.assertEqual(find_Sum([5], 1), 5)

    def test_boundary_case_empty_array(self):
        self.assertEqual(find_Sum([], 0), 0)

    def test_boundary_case_negative_numbers(self):
        self.assertEqual(find_Sum([-1, -2, -3, -4, -5], 5), -3)

    def test_invalid_input_type(self):
        with self.assertRaises(TypeError):
            find_Sum("1, 2, 3, 4, 5", 5)

    def test_invalid_input_negative_length(self):
        with self.assertRaises(ValueError):
            find_Sum([1, 2, 3, 4, 5], -1)
