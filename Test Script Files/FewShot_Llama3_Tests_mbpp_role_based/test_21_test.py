import unittest
from mbpp_21_code import multiples_of_num

class TestMultiplesOfNum(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(multiples_of_num(2, 10), [0, 2, 4, 6, 8, 10, 12, 14, 16, 18])

    def test_edge_case_m_zero(self):
        self.assertEqual(multiples_of_num(0, 10), [])

    def test_edge_case_n_zero(self):
        self.assertEqual(multiples_of_num(2, 0), [])

    def test_edge_case_m_negative(self):
        with self.assertRaises(ValueError):
            multiples_of_num(-2, 10)

    def test_edge_case_n_negative(self):
        with self.assertRaises(ValueError):
            multiples_of_num(2, -10)

    def test_edge_case_m_and_n_zero(self):
        self.assertEqual(multiples_of_num(0, 0), [])
