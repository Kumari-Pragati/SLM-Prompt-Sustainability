import unittest
from mbpp_934_code import dealnnoy_num

class TestDealnnoyNum(unittest.TestCase):
    def test_zero(self):
        self.assertEqual(dealnnoy_num(0, 0), 1)
        self.assertEqual(dealnnoy_num(0, n), 1 for n in range(1, 10))

    def test_positive_numbers(self):
        self.assertEqual(dealnnoy_num(1, 1), 1)
        self.assertEqual(dealnnoy_num(1, n), 2 for n in range(2, 10))
        self.assertEqual(dealnnoy_num(n, 1), 2 for n in range(2, 10))

    def test_negative_numbers(self):
        self.assertEqual(dealnnoy_num(-1, -1), 1)
        self.assertEqual(dealnnoy_num(-1, n), 2 for n in range(1, 10))
        self.assertEqual(dealnnoy_num(n, -1), 2 for n in range(1, 10))
