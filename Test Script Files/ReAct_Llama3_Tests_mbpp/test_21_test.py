import unittest
from mbpp_21_code import multiples_of_num

class TestMultiplesOfNum(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(multiples_of_num(2, 10), [0, 2, 4, 6, 8, 10])

    def test_edge_case_m_zero(self):
        self.assertEqual(multiples_of_num(0, 10), [])

    def test_edge_case_n_zero(self):
        self.assertEqual(multiples_of_num(2, 0), [])

    def test_edge_case_m_one(self):
        self.assertEqual(multiples_of_num(1, 10), [0, 10])

    def test_edge_case_n_one(self):
        self.assertEqual(multiples_of_num(2, 1), [])

    def test_edge_case_m_negative(self):
        with self.assertRaises(TypeError):
            multiples_of_num(-2, 10)

    def test_edge_case_n_negative(self):
        with self.assertRaises(TypeError):
            multiples_of_num(2, -10)
