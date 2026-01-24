import unittest
from mbpp_93_code import power

class TestPowerFunction(unittest.TestCase):

    def test_power_with_zero_exponent(self):
        self.assertEqual(power(2, 0), 1)
        self.assertEqual(power(0, 0), 1)

    def test_power_with_positive_exponent(self):
        self.assertEqual(power(2, 3), 8)
        self.assertEqual(power(5, 1), 5)

    def test_power_with_negative_exponent(self):
        self.assertAlmostEqual(power(2, -1), 0.5)
        self.assertAlmostEqual(power(2, -2), 0.25)

    def test_power_with_zero_base(self):
        self.assertEqual(power(0, 2), 0)
        self.assertEqual(power(0, 3), 0)

    def test_power_with_invalid_inputs(self):
        with self.assertRaises(TypeError):
            power("a", 2)
        with self.assertRaises(TypeError):
            power(2, "b")
        with self.assertRaises(TypeError):
            power("a", "b")
