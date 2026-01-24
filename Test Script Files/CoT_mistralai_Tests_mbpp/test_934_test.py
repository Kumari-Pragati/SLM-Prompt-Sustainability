import unittest
from934_code import dealnnoy_num

class TestDealnnoyNum(unittest.TestCase):
    def test_dealnnoy_num_base_case(self):
        self.assertEqual(dealnnoy_num(1, 1), 1)
        self.assertEqual(dealnnoy_num(2, 2), 3)
        self.assertEqual(dealnnoy_num(3, 3), 7)

    def test_dealnnoy_num_positive_n_zero_m(self):
        self.assertEqual(dealnnoy_num(4, 0), 1)

    def test_dealnnoy_num_zero_n_positive_m(self):
        self.assertEqual(dealnnoy_num(0, 3), 1)

    def test_dealnnoy_num_negative_n_positive_m(self):
        self.assertRaises(ValueError, dealnnoy_num, -1, 3)

    def test_dealnnoy_num_negative_m_positive_n(self):
        self.assertRaises(ValueError, dealnnoy_num, 3, -1)
