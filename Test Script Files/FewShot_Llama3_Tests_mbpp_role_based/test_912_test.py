import unittest
from mbpp_912_code import lobb_num

class TestLobbNum(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(lobb_num(2, 1), 3)

    def test_edge_case_n_zero(self):
        self.assertEqual(lobb_num(0, 1), 1)

    def test_edge_case_m_zero(self):
        self.assertEqual(lobb_num(2, 0), 1)

    def test_edge_case_n_and_m_zero(self):
        self.assertEqual(lobb_num(0, 0), 1)

    def test_invalid_input_n_negative(self):
        with self.assertRaises(ValueError):
            lobb_num(-1, 1)

    def test_invalid_input_m_negative(self):
        with self.assertRaises(ValueError):
            lobb_num(2, -1)

    def test_invalid_input_n_and_m_negative(self):
        with self.assertRaises(ValueError):
            lobb_num(-1, -1)
