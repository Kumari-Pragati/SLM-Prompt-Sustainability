import unittest
from mbpp_856_code import find_Min_Swaps

class TestFindMinSwaps(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(find_Min_Swaps([0, 1, 1, 0, 1], 5), 2)

    def test_edge_case_zero(self):
        self.assertEqual(find_Min_Swaps([0, 0, 0, 0, 0], 5), 5)

    def test_edge_case_all_one(self):
        self.assertEqual(find_Min_Swaps([1, 1, 1, 1, 1], 5), 0)

    def test_edge_case_single_element(self):
        self.assertEqual(find_Min_Swaps([0], 1), 1)

    def test_edge_case_empty_array(self):
        self.assertEqual(find_Min_Swaps([], 0), 0)

    def test_invalid_input_array_length_zero(self):
        with self.assertRaises(IndexError):
            find_Min_Swaps([], 0)

    def test_invalid_input_array_length_negative(self):
        with self.assertRaises(IndexError):
            find_Min_Swaps([0, 1, 1, 0, 1], -5)
