import unittest
from mbpp_347_code import count_Squares

class TestCountSquares(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(count_Squares(2, 3), 6)

    def test_edge_case_m_equal_n(self):
        self.assertEqual(count_Squares(3, 3), 6)

    def test_edge_case_m_greater_n(self):
        self.assertEqual(count_Squares(5, 3), 9)

    def test_edge_case_m_equal_n_and_n_zero(self):
        self.assertEqual(count_Squares(0, 0), 0)

    def test_edge_case_m_greater_n_and_n_zero(self):
        self.assertEqual(count_Squares(5, 0), 0)

    def test_edge_case_m_equal_n_and_m_zero(self):
        self.assertEqual(count_Squares(0, 3), 0)

    def test_edge_case_m_greater_n_and_m_zero(self):
        self.assertEqual(count_Squares(5, 3), 6)

    def test_edge_case_m_equal_n_and_m_n(self):
        self.assertEqual(count_Squares(3, 3), 6)

    def test_edge_case_m_greater_n_and_m_n(self):
        self.assertEqual(count_Squares(5, 3), 6)

    def test_edge_case_m_equal_n_and_m_n_and_n_zero(self):
        self.assertEqual(count_Squares(3, 3), 6)

    def test_edge_case_m_greater_n_and_m_n_and_n_zero(self):
        self.assertEqual(count_Squares(5, 3), 6)
