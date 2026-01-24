import unittest
from mbpp_76_code import count_Squares

class TestCountSquares(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(count_Squares(5, 5), 30)

    def test_edge_case_m_equal_n(self):
        self.assertEqual(count_Squares(5, 5), 30)

    def test_edge_case_m_greater_than_n(self):
        self.assertEqual(count_Squares(5, 3), 14)

    def test_edge_case_m_equal_n_zero(self):
        self.assertEqual(count_Squares(0, 0), 0)

    def test_edge_case_m_greater_than_n_zero(self):
        self.assertEqual(count_Squares(5, 0), 0)

    def test_edge_case_m_equal_n_negative(self):
        with self.assertRaises(ValueError):
            count_Squares(-5, -5)

    def test_edge_case_m_greater_than_n_negative(self):
        with self.assertRaises(ValueError):
            count_Squares(-5, 5)

    def test_edge_case_m_equal_n_negative_zero(self):
        with self.assertRaises(ValueError):
            count_Squares(0, -5)

    def test_edge_case_m_greater_than_n_negative_zero(self):
        with self.assertRaises(ValueError):
            count_Squares(-5, 0)
