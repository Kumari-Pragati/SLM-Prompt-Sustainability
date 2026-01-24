import unittest
from mbpp_589_code import perfect_squares

class TestPerfectSquares(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(perfect_squares(1, 10), [1, 4, 9])
        self.assertEqual(perfect_squares(20, 30), [25])

    def test_edge_cases(self):
        self.assertEqual(perfect_squares(1, 1), [1])
        self.assertEqual(perfect_squares(100, 100), [])
        self.assertEqual(perfect_squares(0, 0), [])

    def test_negative_numbers(self):
        self.assertEqual(perfect_squares(-10, 10), [1, 4, 9])
        self.assertEqual(perfect_squares(-20, -10), [])

    def test_large_numbers(self):
        self.assertEqual(perfect_squares(10000, 10100), [10001])
        self.assertEqual(perfect_squares(1000000, 1001000), [])
