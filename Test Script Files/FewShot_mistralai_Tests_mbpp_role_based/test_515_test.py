import unittest
from mbpp_515_code import modular_sum

class TestModularSum(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertTrue(modular_sum([1, 2, 3], 3, 5))
        self.assertTrue(modular_sum([1, 2, 3], 4, 5))
        self.assertFalse(modular_sum([1, 2, 3], 6, 5))

    def test_zero(self):
        self.assertTrue(modular_sum([0], 0, 0))
        self.assertFalse(modular_sum([0], 1, 0))

    def test_negative_numbers(self):
        self.assertFalse(modular_sum([-1, -2, -3], 3, 5))
        self.assertFalse(modular_sum([-1, -2, -3], 4, 5))
        self.assertTrue(modular_sum([-1, -2, -3], 6, 5))

    def test_empty_list(self):
        self.assertTrue(modular_sum([], 0, 0))

    def test_invalid_input_arr(self):
        with self.assertRaises(TypeError):
            modular_sum(1.5, 3, 5)

    def test_invalid_input_n(self):
        with self.assertRaises(ValueError):
            modular_sum([1, 2, 3], -1, 5)

    def test_invalid_input_m(self):
        with self.assertRaises(ValueError):
            modular_sum([1, 2, 3], 3, -1)
