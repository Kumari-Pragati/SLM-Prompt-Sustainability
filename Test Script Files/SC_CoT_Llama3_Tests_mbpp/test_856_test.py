import unittest
from mbpp_856_code import find_Min_Swaps

class TestFindMinSwaps(unittest.TestCase):
    def test_typical_input(self):
        self.assertEqual(find_Min_Swaps([0, 0, 1, 0, 1], 5), 2)

    def test_edge_case_all_zeros(self):
        self.assertEqual(find_Min_Swaps([0, 0, 0, 0, 0], 5), 5)

    def test_edge_case_all_ones(self):
        self.assertEqual(find_Min_Swaps([1, 1, 1, 1, 1], 5), 0)

    def test_edge_case_single_zero(self):
        self.assertEqual(find_Min_Swaps([0, 1, 1, 1, 1], 5), 1)

    def test_edge_case_single_one(self):
        self.assertEqual(find_Min_Swaps([1, 0, 1, 1, 1], 5), 1)

    def test_edge_case_zero_at_end(self):
        self.assertEqual(find_Min_Swaps([1, 1, 1, 0, 1], 5), 1)

    def test_edge_case_one_at_end(self):
        self.assertEqual(find_Min_Swaps([1, 1, 1, 1, 0], 5), 1)

    def test_invalid_input_non_integer_length(self):
        with self.assertRaises(TypeError):
            find_Min_Swaps([0, 0, 1, 0, 1], 'five')

    def test_invalid_input_non_list_input(self):
        with self.assertRaises(TypeError):
            find_Min_Swaps('not a list', 5)
