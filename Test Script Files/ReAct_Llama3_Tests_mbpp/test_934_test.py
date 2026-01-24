import unittest
from mbpp_934_code import dealnnoy_num

class TestDealnnoyNum(unittest.TestCase):
    def test_zero_m(self):
        self.assertEqual(dealnnoy_num(0, 0), 1)

    def test_zero_n(self):
        self.assertEqual(dealnnoy_num(1, 0), 1)

    def test_zero_n_and_m(self):
        self.assertEqual(dealnnoy_num(0, 0), 1)

    def test_edge_case_m(self):
        self.assertEqual(dealnnoy_num(1, 1), 2)

    def test_edge_case_n(self):
        self.assertEqual(dealnnoy_num(2, 1), 2)

    def test_positive_m_and_n(self):
        self.assertEqual(dealnnoy_num(3, 2), 6)

    def test_negative_m_and_n(self):
        self.assertEqual(dealnnoy_num(-1, -2), 2)
