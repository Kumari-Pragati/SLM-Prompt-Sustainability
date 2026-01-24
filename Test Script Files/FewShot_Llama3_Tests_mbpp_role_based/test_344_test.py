import unittest
from mbpp_344_code import count_Odd_Squares

class TestCountOddSquares(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(count_Odd_Squares(1, 9), 1)

    def test_edge_case_n_zero(self):
        self.assertEqual(count_Odd_Squares(0, 9), 1)

    def test_edge_case_m_zero(self):
        self.assertEqual(count_Odd_Squares(1, 0), 0)

    def test_edge_case_n_negative(self):
        with self.assertRaises(ValueError):
            count_Odd_Squares(-1, 9)

    def test_edge_case_m_negative(self):
        with self.assertRaises(ValueError):
            count_Odd_Squares(1, -9)

    def test_edge_case_n_zero_and_m_zero(self):
        self.assertEqual(count_Odd_Squares(0, 0), 0)

    def test_edge_case_n_large_and_m_large(self):
        self.assertEqual(count_Odd_Squares(100, 1000), 10)
