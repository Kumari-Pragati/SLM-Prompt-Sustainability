import unittest
from mbpp_934_code import dealnnoy_num

class TestDealnnoyNum(unittest.TestCase):

    def test_dealnnoy_num_base_case(self):
        self.assertEqual(dealnnoy_num(0, 0), 1)

    def test_dealnnoy_num_positive_m(self):
        self.assertEqual(dealnnoy_num(1, 1), 2)
        self.assertEqual(dealnnoy_num(2, 1), 3)
        self.assertEqual(dealnnoy_num(3, 1), 5)

    def test_dealnnoy_num_positive_n(self):
        self.assertEqual(dealnnoy_num(1, 2), 3)
        self.assertEqual(dealnnoy_num(2, 2), 6)
        self.assertEqual(dealnnoy_num(3, 2), 10)

    def test_dealnnoy_num_negative_m(self):
        self.assertEqual(dealnnoy_num(-1, 1), 2)
        self.assertEqual(dealnnoy_num(-2, 1), 3)
        self.assertEqual(dealnnoy_num(-3, 1), 5)

    def test_dealnnoy_num_negative_n(self):
        self.assertEqual(dealnnoy_num(1, -1), 2)
        self.assertEqual(dealnnoy_num(2, -1), 3)
        self.assertEqual(dealnnoy_num(3, -1), 5)

    def test_dealnnoy_num_edge_case(self):
        self.assertEqual(dealnnoy_num(0, 1), 1)
        self.assertEqual(dealnnoy_num(1, 0), 1)
