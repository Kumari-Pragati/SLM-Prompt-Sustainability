import unittest
from mbpp_21_code import multiples_of_num

class TestMultiplesOfNum(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(multiples_of_num(2, 10), [2, 4, 6, 8, 10])

    def test_edge_case_m(self):
        self.assertEqual(multiples_of_num(3, 5), [])

    def test_edge_case_n(self):
        self.assertEqual(multiples_of_num(2, 1), [])

    def test_edge_case_m_n(self):
        self.assertEqual(multiples_of_num(2, 2), [2])

    def test_edge_case_m_zero(self):
        with self.assertRaises(ZeroDivisionError):
            multiples_of_num(0, 10)

    def test_edge_case_n_zero(self):
        self.assertEqual(multiples_of_num(2, 0), [])

    def test_edge_case_m_negative(self):
        self.assertEqual(multiples_of_num(-2, 10), [])

    def test_edge_case_n_negative(self):
        self.assertEqual(multiples_of_num(2, -10), [])

    def test_edge_case_m_n_negative(self):
        self.assertEqual(multiples_of_num(-2, -10), [])
