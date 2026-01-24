import unittest
from mbpp_724_code import power_base_sum

class TestPowerBaseSum(unittest.TestCase):

    def test_base_and_power_are_positive_integers(self):
        self.assertRaises(ValueError, power_base_sum, -2, 3)
        self.assertRaises(ValueError, power_base_sum, 2, -3)
        self.assertRaises(TypeError, power_base_sum, 2.5, 3)
        self.assertRaises(TypeError, power_base_sum, 2, 3.5)

    def test_base_and_power_are_integers(self):
        self.assertEqual(power_base_sum(2, 3), 8)
        self.assertEqual(power_base_sum(3, 2), 18)
        self.assertEqual(power_base_sum(5, 4), 91)
        self.assertEqual(power_base_sum(7, 5), 283)

    def test_base_is_1(self):
        self.assertEqual(power_base_sum(1, 3), 1)
        self.assertEqual(power_base_sum(1, 2), 1)
        self.assertEqual(power_base_sum(1, 4), 1)
        self.assertEqual(power_base_sum(1, 5), 1)

    def test_base_is_zero(self):
        self.assertEqual(power_base_sum(0, 3), 0)
        self.assertEqual(power_base_sum(0, 2), 0)
        self.assertEqual(power_base_sum(0, 4), 0)
        self.assertEqual(power_base_sum(0, 5), 0)
