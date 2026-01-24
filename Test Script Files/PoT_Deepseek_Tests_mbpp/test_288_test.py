import unittest
from mbpp_288_code import modular_inverse

class TestModularInverse(unittest.TestCase):

    def test_typical_case(self):
        arr = [2, 3, 4, 5]
        N = len(arr)
        P = 7
        self.assertEqual(modular_inverse(arr, N, P), 2)

    def test_edge_case_with_single_element(self):
        arr = [2]
        N = len(arr)
        P = 7
        self.assertEqual(modular_inverse(arr, N, P), 0)

    def test_boundary_case_with_empty_array(self):
        arr = []
        N = len(arr)
        P = 7
        self.assertEqual(modular_inverse(arr, N, P), 0)

    def test_corner_case_with_negative_elements(self):
        arr = [-2, -3, 4, 5]
        N = len(arr)
        P = 7
        self.assertEqual(modular_inverse(arr, N, P), 2)

    def test_corner_case_with_large_numbers(self):
        arr = [1000, 2000, 3000, 4000]
        N = len(arr)
        P = 7
        self.assertEqual(modular_inverse(arr, N, P), 0)

    def test_exceptional_case_with_zero_modulus(self):
        arr = [2, 3, 4, 5]
        N = len(arr)
        P = 0
        with self.assertRaises(ZeroDivisionError):
            modular_inverse(arr, N, P)
