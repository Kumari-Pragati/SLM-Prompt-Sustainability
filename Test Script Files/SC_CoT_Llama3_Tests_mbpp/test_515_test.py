import unittest
from mbpp_515_code import modular_sum

class TestModularSum(unittest.TestCase):
    def test_typical_input(self):
        self.assertTrue(modular_sum([1, 2, 3], 3, 4))

    def test_edge_case_n_equal_m(self):
        self.assertTrue(modular_sum([1, 2, 3], 4, 4))

    def test_edge_case_n_greater_than_m(self):
        self.assertFalse(modular_sum([1, 2, 3], 5, 4))

    def test_special_case_all_zeros(self):
        self.assertFalse(modular_sum([0, 0, 0], 3, 4))

    def test_special_case_all_ones(self):
        self.assertTrue(modular_sum([1, 1, 1], 3, 4))

    def test_invalid_input_negative_n(self):
        with self.assertRaises(TypeError):
            modular_sum([-1, 2, 3], -1, 4)

    def test_invalid_input_negative_m(self):
        with self.assertRaises(TypeError):
            modular_sum([1, 2, 3], 3, -1)

    def test_invalid_input_non_integer_n(self):
        with self.assertRaises(TypeError):
            modular_sum([1, 2, 3], 3.5, 4)

    def test_invalid_input_non_integer_m(self):
        with self.assertRaises(TypeError):
            modular_sum([1, 2, 3], 3, 4.5)
