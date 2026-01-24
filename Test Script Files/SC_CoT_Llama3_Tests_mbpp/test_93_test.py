import unittest
from mbpp_93_code import power

class TestPowerFunction(unittest.TestCase):
    def test_zero_power(self):
        self.assertEqual(power(0, 0), 1)
        self.assertEqual(power(0, 1), 0)
        self.assertEqual(power(0, 2), 0)
        self.assertEqual(power(0, 3), 0)

    def test_non_zero_power(self):
        self.assertEqual(power(2, 0), 1)
        self.assertEqual(power(2, 1), 2)
        self.assertEqual(power(2, 2), 4)
        self.assertEqual(power(2, 3), 8)

    def test_power_of_one(self):
        self.assertEqual(power(1, 0), 1)
        self.assertEqual(power(1, 1), 1)
        self.assertEqual(power(1, 2), 1)
        self.assertEqual(power(1, 3), 1)

    def test_negative_power(self):
        self.assertEqual(power(-2, 0), 1)
        self.assertEqual(power(-2, 1), -2)
        self.assertEqual(power(-2, 2), 4)
        self.assertEqual(power(-2, 3), -8)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            power("a", 2)
        with self.assertRaises(TypeError):
            power(2, "b")
