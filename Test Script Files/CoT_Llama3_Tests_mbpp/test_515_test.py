import unittest
from mbpp_515_code import modular_sum

class TestModularSum(unittest.TestCase):

    def test_typical_case(self):
        self.assertTrue(modular_sum([1, 2, 3], 3, 5))

    def test_edge_case_n_eq_m(self):
        self.assertTrue(modular_sum([1, 2, 3], 5, 5))

    def test_edge_case_n_lt_m(self):
        self.assertFalse(modular_sum([1, 2, 3], 2, 5))

    def test_edge_case_arr_empty(self):
        self.assertFalse(modular_sum([], 3, 5))

    def test_edge_case_n_eq_0(self):
        self.assertFalse(modular_sum([], 0, 5))

    def test_edge_case_m_eq_0(self):
        with self.assertRaises(ZeroDivisionError):
            modular_sum([1, 2, 3], 3, 0)

    def test_invalid_input_type(self):
        with self.assertRaises(TypeError):
            modular_sum("hello", 3, 5)

    def test_invalid_input_type2(self):
        with self.assertRaises(TypeError):
            modular_sum([1, 2, 3], "hello", 5)

    def test_invalid_input_type3(self):
        with self.assertRaises(TypeError):
            modular_sum([1, 2, 3], 3, "hello")
