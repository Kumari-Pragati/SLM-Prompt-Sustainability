import unittest
from mbpp_934_code import dealnnoy_num

class TestDealnnoyNum(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(dealnnoy_num(3, 3), 27)

    def test_edge_case_m_zero(self):
        self.assertEqual(dealnnoy_num(3, 0), 1)

    def test_edge_case_n_zero(self):
        self.assertEqual(dealnnoy_num(0, 3), 1)

    def test_edge_case_m_n_zero(self):
        self.assertEqual(dealnnoy_num(0, 0), 1)

    def test_edge_case_m_negative(self):
        with self.assertRaises(TypeError):
            dealnnoy_num(-1, 3)

    def test_edge_case_n_negative(self):
        with self.assertRaises(TypeError):
            dealnnoy_num(3, -1)

    def test_edge_case_m_n_negative(self):
        with self.assertRaises(TypeError):
            dealnnoy_num(-1, -1)
