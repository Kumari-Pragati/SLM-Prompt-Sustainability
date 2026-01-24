import unittest
from mbpp_21_code import multiples_of_num

class TestMultiplesOfNum(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(multiples_of_num(2, 10), [0, 2, 4, 6, 8, 10])

    def test_edge_case_m_equal_n(self):
        self.assertEqual(multiples_of_num(5, 5), [])

    def test_edge_case_m_greater_than_n(self):
        self.assertEqual(multiples_of_num(10, 5), [0, 5, 10])

    def test_edge_case_n_equal_zero(self):
        with self.assertRaises(ValueError):
            multiples_of_num(5, 0)

    def test_edge_case_m_equal_zero(self):
        with self.assertRaises(ValueError):
            multiples_of_num(0, 5)

    def test_edge_case_n_negative(self):
        with self.assertRaises(ValueError):
            multiples_of_num(5, -5)

    def test_edge_case_m_negative(self):
        with self.assertRaises(ValueError):
            multiples_of_num(-5, 5)
