import unittest
from mbpp_288_code import modular_inverse

class TestModularInverse(unittest.TestCase):
    def test_typical_use_case(self):
        arr = [2, 3, 4, 5]
        N = len(arr)
        P = 7
        self.assertEqual(modular_inverse(arr, N, P), 2)

    def test_edge_condition(self):
        arr = []
        N = 0
        P = 7
        self.assertEqual(modular_inverse(arr, N, P), 0)

    def test_boundary_condition(self):
        arr = [1]
        N = 1
        P = 7
        self.assertEqual(modular_inverse(arr, N, P), 0)

    def test_invalid_input(self):
        arr = [1, 2, 3]
        N = 3
        P = 0
        with self.assertRaises(ZeroDivisionError):
            modular_inverse(arr, N, P)
