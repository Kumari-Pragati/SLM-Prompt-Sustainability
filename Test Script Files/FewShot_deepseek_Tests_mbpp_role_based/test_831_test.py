import unittest
from mbpp_831_code import count_Pairs

class TestCountPairs(unittest.TestCase):
    def test_typical_use_case(self):
        arr = [1, 2, 3, 2, 1]
        n = len(arr)
        self.assertEqual(count_Pairs(arr, n), 2)

    def test_edge_case_single_element(self):
        arr = [1]
        n = len(arr)
        self.assertEqual(count_Pairs(arr, n), 0)

    def test_boundary_case_empty_array(self):
        arr = []
        n = len(arr)
        self.assertEqual(count_Pairs(arr, n), 0)

    def test_boundary_case_large_array(self):
        arr = [1] * 10000
        n = len(arr)
        self.assertEqual(count_Pairs(arr, n), 49995000)

    def test_invalid_input_negative_number(self):
        arr = [-1, 2, 3, 2, 1]
        n = len(arr)
        with self.assertRaises(Exception):
            count_Pairs(arr, n)

    def test_invalid_input_non_integer(self):
        arr = [1, 2, 'a', 2, 1]
        n = len(arr)
        with self.assertRaises(Exception):
            count_Pairs(arr, n)
