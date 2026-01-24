import unittest
from mbpp_856_code import find_Min_Swaps

class TestFindMinSwaps(unittest.TestCase):
    def test_simple_valid_input(self):
        self.assertEqual(find_Min_Swaps([0, 1, 0, 1], 4), 2)

    def test_edge_case_zero_array(self):
        self.assertEqual(find_Min_Swaps([0, 0, 0, 0], 4), 4)

    def test_edge_case_all_ones_array(self):
        self.assertEqual(find_Min_Swaps([1, 1, 1, 1], 4), 0)

    def test_edge_case_single_element_array(self):
        self.assertEqual(find_Min_Swaps([0], 1), 0)

    def test_edge_case_empty_array(self):
        with self.assertRaises(IndexError):
            find_Min_Swaps([], 0)

    def test_edge_case_invalid_input_type(self):
        with self.assertRaises(TypeError):
            find_Min_Swaps("hello", 4)

    def test_edge_case_invalid_input_length(self):
        with self.assertRaises(IndexError):
            find_Min_Swaps([0, 1], 3)

    def test_edge_case_invalid_input_value(self):
        with self.assertRaises(IndexError):
            find_Min_Swaps([0, 1, 2, 3], 4)
