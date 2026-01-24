import unittest
from mbpp_515_code import modular_sum

class TestModularSum(unittest.TestCase):

    def test_modular_sum_true(self):
        self.assertTrue(modular_sum([1, 2, 3], 3, 4))

    def test_modular_sum_false(self):
        self.assertFalse(modular_sum([1, 2, 3], 3, 3))

    def test_modular_sum_empty_array(self):
        self.assertFalse(modular_sum([], 0, 4))

    def test_modular_sum_single_element_array(self):
        self.assertFalse(modular_sum([1], 1, 4))

    def test_modular_sum_zero_n(self):
        self.assertFalse(modular_sum([1], 0, 4))

    def test_modular_sum_zero_m(self):
        self.assertFalse(modular_sum([1], 3, 0))

    def test_modular_sum_negative_n(self):
        self.assertFalse(modular_sum([-1, 2, 3], 3, 4))

    def test_modular_sum_negative_m(self):
        self.assertFalse(modular_sum([1, 2, 3], 3, -4))

    def test_modular_sum_large_array(self):
        self.assertFalse(modular_sum([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 10, 11))
