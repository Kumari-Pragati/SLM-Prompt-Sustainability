import unittest
from mbpp_515_code import modular_sum

class TestModularSum(unittest.TestCase):
    def test_typical_case(self):
        arr = [1, 2, 3]
        n = len(arr)
        m = 5
        self.assertTrue(modular_sum(arr, n, m))

    def test_boundary_case(self):
        arr = [0]
        n = len(arr)
        m = 1
        self.assertTrue(modular_sum(arr, n, m))

    def test_edge_case(self):
        arr = [1, 2, 3]
        n = len(arr)
        m = 0
        self.assertFalse(modular_sum(arr, n, m))

    def test_invalid_input(self):
        arr = [1, 2, 3]
        n = len(arr)
        m = 'a'
        with self.assertRaises(TypeError):
            modular_sum(arr, n, m)
