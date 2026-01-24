import unittest
from mbpp_93_code import power

class TestPowerFunction(unittest.TestCase):

    def test_power_basic(self):
        self.assertEqual(power(2, 3), 8)
        self.assertEqual(power(5, 0), 1)
        self.assertEqual(power(0, 5), 0)

    def test_power_edge(self):
        self.assertEqual(power(2, 1), 2)
        self.assertEqual(power(0, 0), 1)

    def test_power_boundary(self):
        self.assertEqual(power(2, 31), 2**31)
        self.assertEqual(power(-2, 3), -8)
        self.assertEqual(power(-2, 4), 16)

    def test_power_complex(self):
        self.assertEqual(power(2, 10), 1024)
        self.assertEqual(power(3, 4), 81)
