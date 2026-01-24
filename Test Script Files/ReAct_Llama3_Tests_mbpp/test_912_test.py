import unittest
from mbpp_912_code import lobb_num

class TestLobbNum(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(lobb_num(1, 1), 2)

    def test_edge_case_n_zero(self):
        self.assertEqual(lobb_num(0, 1), 1)

    def test_edge_case_m_zero(self):
        self.assertEqual(lobb_num(1, 0), 1)

    def test_edge_case_n_and_m_zero(self):
        self.assertEqual(lobb_num(0, 0), 1)

    def test_edge_case_n_and_m_negative(self):
        with self.assertRaises(ValueError):
            lobb_num(-1, -1)

    def test_edge_case_n_zero_and_m_positive(self):
        self.assertEqual(lobb_num(0, 1), 1)

    def test_edge_case_m_zero_and_n_positive(self):
        self.assertEqual(lobb_num(1, 0), 1)

    def test_edge_case_n_and_m_large(self):
        self.assertEqual(lobb_num(10, 5), 462)
