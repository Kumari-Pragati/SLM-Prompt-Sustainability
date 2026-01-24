import unittest
from mbpp_955_code import is_abundant

class TestIsAbundant(unittest.TestCase):

    def test_normal_input(self):
        self.assertTrue(is_abundant(12))
        self.assertTrue(is_abundant(28))

    def test_edge_and_boundary_conditions(self):
        self.assertFalse(is_abundant(1))
        self.assertFalse(is_abundant(2))
        self.assertTrue(is_abundant(18))
        self.assertTrue(is_abundant(27))
        self.assertFalse(is_abundant(29))
        self.assertTrue(is_abundant(36))

    def test_special_cases(self):
        self.assertFalse(is_abundant(7))  # Perfect number, not abundant
        self.assertTrue(is_abundant(8))  # Abundant number
        self.assertFalse(is_abundant(9))  # Not abundant
        self.assertTrue(is_abundant(10))  # Abundant number
        self.assertFalse(is_abundant(11))  # Not abundant

    def test_invalid_inputs(self):
        self.assertRaises(TypeError, is_abundant, 'not_a_number')
        self.assertRaises(TypeError, is_abundant, -1)
        self.assertRaises(TypeError, is_abundant, 0)
