import unittest
from mbpp_856_code import find_Min_Swaps

class TestFindMinSwaps(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(find_Min_Swaps([0, 1, 0, 1], 4), 2)

    def test_all_zeros(self):
        self.assertEqual(find_Min_Swaps([0, 0, 0, 0], 4), 0)

    def test_all_ones(self):
        self.assertEqual(find_Min_Swaps([1, 1, 1, 1], 4), 0)

    def test_boundary_case(self):
        self.assertEqual(find_Min_Swaps([0], 1), 0)

    def test_edge_case_with_one_zero(self):
        self.assertEqual(find_Min_Swaps([1, 0, 1], 3), 1)

    def test_edge_case_with_two_zeros(self):
        self.assertEqual(find_Min_Swaps([1, 0, 0, 1], 4), 2)

    def test_invalid_input_empty_list(self):
        with self.assertRaises(Exception):
            find_Min_Swaps([], 0)

    def test_invalid_input_negative_values(self):
        with self.assertRaises(Exception):
            find_Min_Swaps([-1, 0, 1], 3)

    def test_invalid_input_non_integer_values(self):
        with self.assertRaises(Exception):
            find_Min_Swaps([0, '1', 0, 1], 4)
