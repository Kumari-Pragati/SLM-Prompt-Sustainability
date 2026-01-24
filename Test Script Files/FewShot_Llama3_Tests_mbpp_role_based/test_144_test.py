import unittest
from mbpp_144_code import sum_Pairs

class TestSumPairs(unittest.TestCase):
    def test_typical_use_case(self):
        arr = [1, 2, 3, 4, 5]
        n = 5
        self.assertEqual(sum_Pairs(arr, n), 15)

    def test_edge_case_n_equal_to_array_length(self):
        arr = [1, 2, 3, 4, 5]
        n = len(arr)
        self.assertEqual(sum_Pairs(arr, n), 0)

    def test_edge_case_n_equal_to_zero(self):
        arr = [1, 2, 3, 4, 5]
        n = 0
        with self.assertRaises(ValueError):
            sum_Pairs(arr, n)

    def test_edge_case_n_greater_than_array_length(self):
        arr = [1, 2, 3, 4, 5]
        n = 6
        with self.assertRaises(ValueError):
            sum_Pairs(arr, n)

    def test_invalid_input_type(self):
        arr = "not a list"
        n = 5
        with self.assertRaises(TypeError):
            sum_Pairs(arr, n)
