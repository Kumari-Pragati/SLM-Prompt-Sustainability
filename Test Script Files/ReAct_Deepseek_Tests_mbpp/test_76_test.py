import unittest
from mbpp_76_code import count_Squares

class TestCountSquares(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(count_Squares(2, 5), 14)

    def test_edge_case_with_same_numbers(self):
        self.assertEqual(count_Squares(5, 5), 14)

    def test_edge_case_with_small_numbers(self):
        self.assertEqual(count_Squares(1, 1), 1)

    def test_edge_case_with_large_numbers(self):
        self.assertEqual(count_Squares(100, 200), 211400)

    def test_order_of_m_and_n_does_not_matter(self):
        self.assertEqual(count_Squares(5, 2), 14)

    def test_negative_numbers(self):
        with self.assertRaises(Exception):
            count_squares(-2, 5)

    def test_non_integer_numbers(self):
        with self.assertRaises(Exception):
            count_squares(2.5, 5)
