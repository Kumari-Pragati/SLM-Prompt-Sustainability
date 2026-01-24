import unittest
from mbpp_93_code import power

class TestPowerFunction(unittest.TestCase):
    def test_zero_to_the_power_of_zero(self):
        self.assertEqual(power(0, 0), 1)

    def test_zero_to_the_power_of_any_number(self):
        for a in range(10):
            self.assertEqual(power(0, a), 0)

    def test_one_to_the_power_of_any_number(self):
        self.assertEqual(power(1, 1), 1)
        for a in range(2, 10):
            self.assertEqual(power(1, a), 1)

    def test_negative_base(self):
        self.assertRaises(ValueError, lambda: power(-1, 2))

    def test_negative_exponent(self):
        self.assertRaises(ValueError, lambda: power(2, -1))

    def test_large_base_and_exponent(self):
        self.assertEqual(power(2, 100), 1073741824)
        self.assertEqual(power(2, 200), 1099511627776)

    def test_large_number_raises_TypeError(self):
        self.assertRaises(TypeError, lambda: power(sys.maxsize + 1, 2))
