import unittest
from mbpp_93_code import power

class TestPowerFunction(unittest.TestCase):

    def test_power_zero(self):
        self.assertEqual(power(2, 0), 1)

    def test_power_zero_a(self):
        self.assertEqual(power(0, 2), 0)

    def test_power_one(self):
        self.assertEqual(power(2, 1), 2)

    def test_power_positive(self):
        self.assertEqual(power(2, 3), 8)

    def test_power_negative(self):
        self.assertEqual(power(-2, 3), -8)

    def test_power_negative_a(self):
        self.assertEqual(power(-2, -3), 8)

    def test_power_non_integer(self):
        self.assertEqual(power(2.5, 3), 15.625)

    def test_power_non_integer_a(self):
        self.assertEqual(power(-2.5, 3), -15.625)

    def test_power_zero_b(self):
        self.assertEqual(power(2, 0), 1)

    def test_power_negative_b(self):
        self.assertEqual(power(-2, -3), 8)

    def test_power_edge_case(self):
        self.assertEqual(power(0, 0), 1)

    def test_power_edge_case_a(self):
        self.assertEqual(power(0, 1), 0)
