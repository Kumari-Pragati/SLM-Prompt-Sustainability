import unittest
from mbpp_589_code import perfect_squares

class TestPerfectSquares(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(perfect_squares(0, 0), [])

    def test_single_element(self):
        self.assertEqual(perfect_squares(1, 1), [1])

    def test_no_perfect_squares(self):
        self.assertEqual(perfect_squares(1, 5), [1, 2, 3, 4, 5])

    def test_perfect_squares(self):
        self.assertEqual(perfect_squares(1, 10), [1, 4, 9])

    def test_large_range(self):
        self.assertEqual(perfect_squares(1, 100), [1, 4, 9, 16, 25, 36, 49, 64, 81, 64, 81, 100])
