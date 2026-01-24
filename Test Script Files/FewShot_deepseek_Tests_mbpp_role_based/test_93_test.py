import unittest
from mbpp_93_code import power

class TestPower(unittest.TestCase):
    def test_power_positive_numbers(self):
        self.assertEqual(power(2, 3), 8)

    def test_power_zero(self):
        self.assertEqual(power(2, 0), 1)

    def test_power_one(self):
        self.assertEqual(power(2, 1), 2)

    def test_power_negative_exponent(self):
        self.assertEqual(power(2, -1), 0.5)

    def test_power_zero_base(self):
        self.assertEqual(power(0, 2), 0)

    def test_power_invalid_input(self):
        with self.assertRaises(TypeError):
            power('a', 2)
