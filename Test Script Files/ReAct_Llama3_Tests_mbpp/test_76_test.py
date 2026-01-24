import unittest
from mbpp_76_code import count_Squares

class TestCountSquares(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(count_Squares(5, 7), 28)

    def test_edge_case_m_equal_n(self):
        self.assertEqual(count_Squares(5, 5), 15)

    def test_edge_case_m_greater_n(self):
        self.assertEqual(count_Squares(7, 5), 28)

    def test_edge_case_m_equal_n_negative(self):
        self.assertEqual(count_Squares(-5, -5), 0)

    def test_edge_case_m_greater_n_negative(self):
        self.assertEqual(count_Squares(-7, -5), 0)

    def test_edge_case_m_equal_n_zero(self):
        self.assertEqual(count_Squares(0, 0), 0)

    def test_edge_case_m_greater_n_zero(self):
        self.assertEqual(count_Squares(0, 5), 0)

    def test_edge_case_m_equal_n_one(self):
        self.assertEqual(count_Squares(1, 1), 1)

    def test_edge_case_m_greater_n_one(self):
        self.assertEqual(count_Squares(1, 5), 3)
