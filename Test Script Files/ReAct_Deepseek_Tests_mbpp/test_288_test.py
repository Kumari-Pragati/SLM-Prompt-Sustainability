import unittest
from mbpp_288_code import modular_inverse

class TestModularInverse(unittest.TestCase):

    def test_typical_case(self):
        arr = [2, 3, 4, 5]
        N = len(arr)
        P = 7
        result = modular_inverse(arr, N, P)
        self.assertEqual(result, 2)

    def test_edge_case_with_single_element(self):
        arr = [2]
        N = len(arr)
        P = 7
        result = modular_inverse(arr, N, P)
        self.assertEqual(result, 0)

    def test_edge_case_with_zero_element(self):
        arr = []
        N = len(arr)
        P = 7
        result = modular_inverse(arr, N, P)
        self.assertEqual(result, 0)

    def test_edge_case_with_negative_element(self):
        arr = [-2, 3, 4, 5]
        N = len(arr)
        P = 7
        with self.assertRaises(Exception):
            modular_inverse(arr, N, P)

    def test_edge_case_with_zero_modulus(self):
        arr = [2, 3, 4, 5]
        N = len(arr)
        P = 0
        with self.assertRaises(Exception):
            modular_inverse(arr, N, P)
