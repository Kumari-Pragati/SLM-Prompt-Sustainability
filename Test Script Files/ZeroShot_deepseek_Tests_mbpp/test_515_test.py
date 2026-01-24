import unittest
from mbpp_515_code import modular_sum

class TestModularSum(unittest.TestCase):

    def test_true_cases(self):
        self.assertTrue(modular_sum([1, 2, 3], 3, 5))
        self.assertTrue(modular_sum([1, 2, 3, 4], 4, 10))
        self.assertTrue(modular_sum([1, 2, 3, 4, 5], 5, 15))

    def test_false_cases(self):
        self.assertFalse(modular_sum([1, 2, 3], 3, 4))
        self.assertFalse(modular_sum([1, 2, 3, 4], 4, 6))
        self.assertFalse(modular_sum([1, 2, 3, 4, 5], 5, 8))
