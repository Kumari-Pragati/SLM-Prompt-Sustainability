import unittest
from mbpp_515_code import modular_sum

class TestModularSum(unittest.TestCase):

    def test_typical_case(self):
        arr = [1, 2, 3]
        n = len(arr)
        m = 5
        self.assertTrue(modular_sum(arr, n, m))

    def test_edge_case_m_less_than_n(self):
        arr = [1, 2, 3]
        n = len(arr)
        m = 3
        self.assertFalse(modular_sum(arr, n, m))

    def test_edge_case_m_equals_n(self):
        arr = [1, 2, 3]
        n = len(arr)
        m = n
        self.assertFalse(modular_sum(arr, n, m))

    def test_edge_case_empty_array(self):
        arr = []
        n = len(arr)
        m = 5
        self.assertFalse(modular_sum(arr, n, m))

    def test_error_case_negative_numbers(self):
        arr = [-1, -2, -3]
        n = len(arr)
        m = 5
        self.assertFalse(modular_sum(arr, n, m))

    def test_error_case_large_numbers(self):
        arr = [1000, 2000, 3000]
        n = len(arr)
        m = 5
        self.assertFalse(modular_sum(arr, n, m))
