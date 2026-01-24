import unittest
from mbpp_515_code import modular_sum

class TestModularSum(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertTrue(modular_sum([1, 2, 3], 3, 5))

    def test_edge_case_n_equal_m(self):
        self.assertFalse(modular_sum([1, 2, 3], 5, 5))

    def test_edge_case_n_greater_than_m(self):
        self.assertTrue(modular_sum([1, 2, 3], 6, 5))

    def test_edge_case_m_zero(self):
        with self.assertRaises(ZeroDivisionError):
            modular_sum([1, 2, 3], 3, 0)

    def test_invalid_input_non_integer_n(self):
        with self.assertRaises(TypeError):
            modular_sum([1, 2, 3], 'a', 5)

    def test_invalid_input_non_integer_m(self):
        with self.assertRaises(TypeError):
            modular_sum([1, 2, 3], 3, 'b')
