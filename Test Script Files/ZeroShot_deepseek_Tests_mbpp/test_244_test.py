import unittest
from mbpp_244_code import next_Perfect_Square

class TestNextPerfectSquare(unittest.TestCase):

    def test_perfect_square(self):
        self.assertEqual(next_Perfect_Square(1), 4)
        self.assertEqual(next_Perfect_Square(4), 9)
        self.assertEqual(next_Perfect_Square(9), 16)
        self.assertEqual(next_Perfect_Square(16), 25)

    def test_non_perfect_square(self):
        self.assertEqual(next_Perfect_Square(3), 4)
        self.assertEqual(next_Perfect_Square(8), 9)
        self.assertEqual(next_Perfect_Square(15), 16)
        self.assertEqual(next_Perfect_Square(23), 25)

    def test_negative_number(self):
        self.assertEqual(next_Perfect_Square(-1), 1)
        self.assertEqual(next_Perfect_Square(-8), 1)
        self.assertEqual(next_Perfect_Square(-15), 1)
        self.assertEqual(next_Perfect_Square(-23), 1)

    def test_zero(self):
        self.assertEqual(next_Perfect_Square(0), 1)
