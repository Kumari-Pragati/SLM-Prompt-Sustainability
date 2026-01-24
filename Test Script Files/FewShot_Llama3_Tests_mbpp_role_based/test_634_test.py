import unittest
from mbpp_634_code import even_Power_Sum

class TestEvenPowerSum(unittest.TestCase):
    def test_positive_integer(self):
        self.assertEqual(even_Power_Sum(5), 5760)

    def test_zero(self):
        self.assertEqual(even_Power_Sum(0), 0)

    def test_negative_integer(self):
        with self.assertRaises(TypeError):
            even_Power_Sum(-1)

    def test_non_integer(self):
        with self.assertRaises(TypeError):
            even_Power_Sum(3.5)
