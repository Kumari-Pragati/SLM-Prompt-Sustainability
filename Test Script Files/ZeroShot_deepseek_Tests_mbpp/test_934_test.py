import unittest
from mbpp_934_code import dealnnoy_num

class TestDealnnoyNum(unittest.TestCase):

    def test_zero_values(self):
        self.assertEqual(dealnnoy_num(0, 0), 1)
        self.assertEqual(dealnnoy_num(5, 0), 1)
        self.assertEqual(dealnnoy_num(0, 5), 1)

    def test_positive_values(self):
        self.assertEqual(dealnnoy_num(1, 1), 2)
        self.assertEqual(dealnnoy_num(2, 2), 7)
        self.assertEqual(dealnnoy_num(3, 3), 44)

    def test_negative_values(self):
        self.assertEqual(dealnnoy_num(-1, -1), 1)
        self.assertEqual(dealnnoy_num(-2, -2), 1)
        self.assertEqual(dealnnoy_num(-3, -3), 1)
