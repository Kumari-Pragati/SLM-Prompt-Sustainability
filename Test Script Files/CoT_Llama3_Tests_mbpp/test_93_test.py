import unittest
from mbpp_93_code import power

class TestPower(unittest.TestCase):
    def test_power_zero(self):
        self.assertEqual(power(2,0), 1)

    def test_power_zero_a(self):
        self.assertEqual(power(0,2), 0)

    def test_power_one(self):
        self.assertEqual(power(2,1), 2)

    def test_power_positive(self):
        self.assertEqual(power(2,3), 8)

    def test_power_negative(self):
        self.assertEqual(power(-2,3), -8)

    def test_power_negative_a(self):
        self.assertEqual(power(-2,0), 1)

    def test_power_negative_b(self):
        self.assertEqual(power(-2,-3), 8)

    def test_power_invalid_input(self):
        with self.assertRaises(TypeError):
            power('a', 2)

    def test_power_invalid_input_b(self):
        with self.assertRaises(TypeError):
            power(2, 'b')
