import unittest
from mbpp_271_code import even_Power_Sum

class TestEvenPowerSum(unittest.TestCase):

    def test_even_Power_Sum(self):
        self.assertEqual(even_Power_Sum(1), 2^5)
        self.assertEqual(even_Power_Sum(2), 2^5 + 4^5)
        self.assertEqual(even_Power_Sum(3), 2^5 + 4^5 + 6^5)
        self.assertEqual(even_Power_Sum(4), 2^5 + 4^5 + 6^5 + 8^5)
