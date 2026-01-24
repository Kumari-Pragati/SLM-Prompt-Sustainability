import unittest
from mbpp_589_code import perfect_squares

class TestPerfectSquares(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(perfect_squares(1, 10), [1, 4, 9])

    def test_edge_case_a_zero(self):
        self.assertEqual(perfect_squares(0, 10), [])

    def test_edge_case_b_zero(self):
        self.assertEqual(perfect_squares(1, 0), [])

    def test_edge_case_a_equal_b(self):
        self.assertEqual(perfect_squares(1, 1), [1])

    def test_edge_case_a_greater_b(self):
        self.assertEqual(perfect_squares(5, 3), [])

    def test_edge_case_b_greater_a(self):
        self.assertEqual(perfect_squares(3, 5), [])

    def test_edge_case_a_negative(self):
        with self.assertRaises(ValueError):
            perfect_squares(-1, 10)

    def test_edge_case_b_negative(self):
        with self.assertRaises(ValueError):
            perfect_squares(1, -10)

    def test_edge_case_a_and_b_negative(self):
        with self.assertRaises(ValueError):
            perfect_squares(-1, -10)
