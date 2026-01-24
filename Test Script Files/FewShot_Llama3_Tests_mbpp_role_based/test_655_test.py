import unittest
from mbpp_655_code import fifth_Power_Sum

class TestFifthPowerSum(unittest.TestCase):
    def test_positive_integer(self):
        self.assertEqual(fifth_Power_Sum(5), 225)

    def test_zero(self):
        self.assertEqual(fifth_Power_Sum(0), 0)

    def test_negative_integer(self):
        with self.assertRaises(TypeError):
            fifth_Power_Sum(-1)

    def test_non_integer(self):
        with self.assertRaises(TypeError):
            fifth_Power_Sum(3.5)

    def test_large_integer(self):
        self.assertEqual(fifth_Power_Sum(100), 32835000)
