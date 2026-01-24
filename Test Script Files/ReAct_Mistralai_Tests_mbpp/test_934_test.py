import unittest
from934_code import dealnnoy_num

class TestDealennoyNum(unittest.TestCase):

    def test_dealnnoy_num_positive_input(self):
        self.assertEqual(dealnnoy_num(0, 0), 1)
        self.assertEqual(dealnnoy_num(1, 0), 1)
        self.assertEqual(dealnnoy_num(1, 1), 2)
        self.assertEqual(dealnnoy_num(2, 1), 3)
        self.assertEqual(dealnnoy_num(2, 2), 6)
        self.assertEqual(dealnnoy_num(5, 3), 31)
        self.assertEqual(dealnnoy_num(5, 5), 106)

    def test_dealnnoy_num_negative_input(self):
        self.assertEqual(dealnnoy_num(-1, 0), None)
        self.assertEqual(dealnnoy_num(0, -1), None)
        self.assertEqual(dealnnoy_num(-1, -1), 1)

    def test_dealnnoy_num_large_input(self):
        self.assertEqual(dealnnoy_num(100, 50), 14951328320511161964)
        self.assertEqual(dealnnoy_num(50, 100), 14951328320511161964)
