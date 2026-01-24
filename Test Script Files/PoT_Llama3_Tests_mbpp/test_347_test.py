import unittest
from mbpp_347_code import count_Squares

class TestCountSquares(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(count_Squares(3, 4), 30)

    def test_edge_case_m_equal_n(self):
        self.assertEqual(count_Squares(2, 2), 6)

    def test_edge_case_m_greater_n(self):
        self.assertEqual(count_Squares(4, 3), 30)

    def test_edge_case_m_equal_n_zero(self):
        self.assertEqual(count_Squares(0, 0), 0)

    def test_edge_case_m_greater_n_zero(self):
        self.assertEqual(count_Squares(0, 1), 1)

    def test_edge_case_m_equal_n_negative(self):
        with self.assertRaises(ValueError):
            count_Squares(-1, -1)

    def test_edge_case_m_greater_n_negative(self):
        with self.assertRaises(ValueError):
            count_Squares(-1, 1)

    def test_edge_case_m_equal_n_negative_zero(self):
        with self.assertRaises(ValueError):
            count_Squares(0, -1)

    def test_edge_case_m_greater_n_negative_zero(self):
        with self.assertRaises(ValueError):
            count_Squares(-1, 0)
