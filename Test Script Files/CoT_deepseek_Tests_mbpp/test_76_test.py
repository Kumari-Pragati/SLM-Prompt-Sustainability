import unittest
from mbpp_76_code import count_Squares

class TestCountSquares(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(count_Squares(2, 5), 14.0)

    def test_edge_case_n_less_than_m(self):
        self.assertEqual(count_Squares(5, 2), 14.0)

    def test_boundary_case_m_equals_n(self):
        self.assertEqual(count_Squares(3, 3), 4.5)

    def test_boundary_case_m_equals_1(self):
        self.assertEqual(count_Squares(1, 5), 1.0)

    def test_boundary_case_n_equals_1(self):
        self.assertEqual(count_Squares(5, 1), 5.0)

    def test_invalid_input_negative_numbers(self):
        with self.assertRaises(Exception):
            count_Squares(-2, 5)

    def test_invalid_input_zero(self):
        with self.assertRaises(Exception):
            count_Squares(0, 5)
