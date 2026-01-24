import unittest
from mbpp_515_code import modular_sum

class TestModularSum(unittest.TestCase):

    def test_modular_sum_empty_list(self):
        self.assertFalse(modular_sum([], 0, 1))

    def test_modular_sum_single_element(self):
        self.assertFalse(modular_sum([1], 1, 1))
        self.assertTrue(modular_sum([1], 2, 1))
        self.assertTrue(modular_sum([1], 3, 1))

    def test_modular_sum_multiple_elements(self):
        self.assertFalse(modular_sum([1, 2], 3, 3))
        self.assertTrue(modular_sum([1, 2], 4, 3))
        self.assertTrue(modular_sum([1, 2], 5, 3))
        self.assertTrue(modular_sum([1, 2], 6, 3))

        self.assertFalse(modular_sum([1, 2], 3, 2))
        self.assertTrue(modular_sum([1, 2], 4, 2))
        self.assertTrue(modular_sum([1, 2], 5, 2))
        self.assertTrue(modular_sum([1, 2], 6, 2))

        self.assertFalse(modular_sum([1, 2], 3, 4))
        self.assertTrue(modular_sum([1, 2], 4, 4))
        self.assertTrue(modular_sum([1, 2], 5, 4))
        self.assertTrue(modular_sum([1, 2], 6, 4))
