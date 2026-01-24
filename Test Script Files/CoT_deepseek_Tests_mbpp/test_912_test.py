import unittest
from mbpp_912_code import lobb_num

class TestLobbNum(unittest.TestCase):
    def test_typical_case(self):
        self.assertAlmostEqual(lobb_num(3, 2), 10.0)

    def test_edge_case_n_zero(self):
        self.assertAlmostEqual(lobb_num(0, 2), 1.0)

    def test_edge_case_m_zero(self):
        self.assertAlmostEqual(lobb_num(3, 0), 3.0)

    def test_edge_case_n_and_m_zero(self):
        self.assertAlmostEqual(lobb_num(0, 0), 1.0)

    def test_invalid_input_n_negative(self):
        with self.assertRaises(Exception):
            lobb_num(-1, 2)

    def test_invalid_input_m_negative(self):
        with self.assertRaises(Exception):
            lobb_num(3, -2)

    def test_invalid_input_n_and_m_negative(self):
        with self.assertRaises(Exception):
            lobb_num(-3, -2)

    def test_invalid_input_m_greater_than_n(self):
        with self.assertRaises(Exception):
            lobb_num(2, 3)
