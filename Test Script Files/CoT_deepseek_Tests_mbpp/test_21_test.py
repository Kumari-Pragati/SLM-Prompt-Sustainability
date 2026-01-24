import unittest
from mbpp_21_code import multiples_of_num

class TestMultiplesOfNum(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(multiples_of_num(3, 5), [5, 10, 15])

    def test_edge_case_m_less_than_n(self):
        self.assertEqual(multiples_of_num(2, 5), [])

    def test_edge_case_m_equals_n(self):
        self.assertEqual(multiples_of_num(5, 5), [5])

    def test_edge_case_m_equals_zero(self):
        self.assertEqual(multiples_of_num(0, 5), [])

    def test_edge_case_n_equals_zero(self):
        self.assertEqual(multiples_of_num(5, 0), [])

    def test_invalid_input_m_negative(self):
        with self.assertRaises(Exception):
            multiples_of_num(-3, 5)

    def test_invalid_input_n_negative(self):
        with self.assertRaises(Exception):
            multiples_of_num(3, -5)

    def test_invalid_input_both_negative(self):
        with self.assertRaises(Exception):
            multiples_of_num(-3, -5)
