import unittest
from mbpp_347_code import count_Squares

class TestCountSquares(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(count_Squares(2, 3), 14)

    def test_edge_case_with_same_numbers(self):
        self.assertEqual(count_Squares(3, 3), 14)

    def test_edge_case_with_small_numbers(self):
        self.assertEqual(count_Squares(1, 1), 1)

    def test_edge_case_with_large_numbers(self):
        self.assertEqual(count_Squares(100, 200), 166666)

    def test_negative_numbers(self):
        with self.assertRaises(Exception):
            count_Squares(-1, 2)

    def test_non_integer_numbers(self):
        with self.assertRaises(Exception):
            count_Squares(2.5, 3)
