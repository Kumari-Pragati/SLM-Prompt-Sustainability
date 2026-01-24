import unittest
from mbpp_724_code import power_base_sum

class TestPowerBaseSum(unittest.TestCase):

    def test_positive_integer_base_and_power(self):
        self.assertEqual(power_base_sum(2, 3), 8)
        self.assertEqual(power_base_sum(3, 4), 81)
        self.assertEqual(power_base_sum(5, 2), 25)

    def test_zero_base_and_power(self):
        self.assertEqual(power_base_sum(0, 0), 0)
        self.assertEqual(power_base_sum(0, 1), 0)
        self.assertEqual(power_base_sum(0, 2), 0)

    def test_negative_base_and_power(self):
        self.assertEqual(power_base_sum(-2, 3), -8)
        self.assertEqual(power_base_sum(-3, 4), -81)
        self.assertEqual(power_base_sum(-5, 2), -25)

    def test_fractional_base_and_power(self):
        self.assertRaises(ValueError, power_base_sum, 0.5, 2)
        self.assertRaises(ValueError, power_base_sum, 2, 0.5)

    def test_string_base_and_power(self):
        self.assertRaises(TypeError, power_base_sum, 'a', 2)
        self.assertRaises(TypeError, power_base_sum, 2, 'a')
