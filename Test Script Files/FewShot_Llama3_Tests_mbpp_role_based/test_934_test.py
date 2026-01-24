import unittest
from mbpp_934_code import dealnnoy_num

class TestDealnnoyNum(unittest.TestCase):
    def test_zero_m(self):
        self.assertEqual(dealnnoy_num(0, 3), 1)

    def test_zero_n(self):
        self.assertEqual(dealnnoy_noy_num(2, 0), 1)

    def test_positive_m_positive_n(self):
        self.assertEqual(dealnnoy_num(3, 3), 7)

    def test_positive_m_negative_n(self):
        self.assertEqual(dealnnoy_num(3, -1), 3)

    def test_negative_m_positive_n(self):
        self.assertEqual(dealnnoy_num(-1, 3), 3)

    def test_negative_m_negative_n(self):
        self.assertEqual(dealnnoy_num(-1, -1), 1)

    def test_m_zero_n_negative(self):
        self.assertEqual(dealnnoy_num(0, -1), 1)

    def test_m_negative_n_zero(self):
        self.assertEqual(dealnnoy_num(-1, 0), 1)
