import unittest
from mbpp_344_code import count_Odd_Squares

class TestCountOddSquares(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(count_Odd_Squares(1, 4), 1)

    def test_edge_case_n_zero(self):
        self.assertEqual(count_Odd_Squares(0, 4), 2)

    def test_edge_case_m_zero(self):
        self.assertEqual(count_Odd_Squares(1, 0), 0)

    def test_edge_case_n_one(self):
        self.assertEqual(count_Odd_Squares(1, 1), 0)

    def test_edge_case_m_one(self):
        self.assertEqual(count_Odd_Squares(1, 1), 0)

    def test_edge_case_n_and_m_zero(self):
        self.assertEqual(count_Odd_Squares(0, 0), 0)

    def test_edge_case_n_and_m_negative(self):
        with self.assertRaises(ValueError):
            count_Odd_Squares(-1, -4)

    def test_edge_case_n_and_m_non_integer(self):
        with self.assertRaises(TypeError):
            count_Odd_Squares(1.5, 4.5)
