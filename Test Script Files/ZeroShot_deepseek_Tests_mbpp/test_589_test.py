import unittest
from mbpp_589_code import perfect_squares

class TestPerfectSquares(unittest.TestCase):

    def test_perfect_squares(self):
        self.assertEqual(perfect_squares(1, 10), [1, 4, 9])
        self.assertEqual(perfect_squares(10, 20), [16])
        self.assertEqual(perfect_squares(20, 30), [])
        self.assertEqual(perfect_squares(100, 200), [144, 169, 196])
        self.assertEqual(perfect_squares(300, 400), [324])
