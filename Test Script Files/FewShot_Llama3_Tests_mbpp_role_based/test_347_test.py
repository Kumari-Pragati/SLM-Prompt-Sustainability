import unittest
from mbpp_347_code import count_Squares

class TestCountSquares(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(count_Squares(3, 4), 30)

    def test_edge_case_m_equal_n(self):
        self.assertEqual(count_Squares(2, 2), 3)

    def test_edge_case_m_greater_than_n(self):
        self.assertEqual(count_Squares(4, 3), 30)

    def test_edge_case_m_equal_n_zero(self):
        self.assertEqual(count_Squares(0, 0), 0)

    def test_edge_case_m_greater_than_n_zero(self):
        self.assertEqual(count_Squares(4, 0), 0)

    def test_invalid_input_m_negative(self):
        with self.assertRaises(ValueError):
            count_Squares(-1, 4)

    def test_invalid_input_n_negative(self):
        with self.assertRaises(ValueError):
            count_Squares(4, -1)
