import unittest
from mbpp_856_code import find_Min_Swaps

class TestFind_Min_Swaps(unittest.TestCase):
    def test_typical_use_case(self):
        arr = [0, 1, 0, 1, 0]
        n = len(arr)
        self.assertEqual(find_Min_Swaps(arr, n), 2)

    def test_edge_case_all_zeros(self):
        arr = [0, 0, 0, 0, 0]
        n = len(arr)
        self.assertEqual(find_Min_Swaps(arr, n), 5)

    def test_edge_case_all_ones(self):
        arr = [1, 1, 1, 1, 1]
        n = len(arr)
        self.assertEqual(find_Min_Swaps(arr, n), 0)

    def test_edge_case_single_zero(self):
        arr = [0, 1, 1, 1, 1]
        n = len(arr)
        self.assertEqual(find_Min_Swaps(arr, n), 1)

    def test_edge_case_single_one(self):
        arr = [1, 0, 1, 1, 1]
        n = len(arr)
        self.assertEqual(find_Min_Swaps(arr, n), 0)

    def test_invalid_input_empty_array(self):
        arr = []
        n = len(arr)
        with self.assertRaises(IndexError):
            find_Min_Swaps(arr, n)

    def test_invalid_input_array_with_non_integer_elements(self):
        arr = [0, 1, 'a', 1, 0]
        n = len(arr)
        with self.assertRaises(TypeError):
            find_Min_Swaps(arr, n)
