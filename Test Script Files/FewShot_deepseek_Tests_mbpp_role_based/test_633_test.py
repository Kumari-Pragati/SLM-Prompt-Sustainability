import unittest
from mbpp_633_code import pair_OR_Sum

class TestPairOrSum(unittest.TestCase):
    def test_typical_case(self):
        arr = [1, 2, 3, 4]
        n = len(arr)
        self.assertEqual(pair_OR_Sum(arr, n), 28)

    def test_edge_case_single_element(self):
        arr = [5]
        n = len(arr)
        self.assertEqual(pair_OR_Sum(arr, n), 0)

    def test_boundary_case_empty_array(self):
        arr = []
        n = len(arr)
        self.assertEqual(pair_OR_Sum(arr, n), 0)

    def test_invalid_input_negative_number(self):
        arr = [-1, -2, -3, -4]
        n = len(arr)
        self.assertEqual(pair_OR_Sum(arr, n), 56)

    def test_invalid_input_non_integer(self):
        arr = [1, 2, '3', 4]
        n = len(arr)
        with self.assertRaises(TypeError):
            pair_OR_Sum(arr, n)
