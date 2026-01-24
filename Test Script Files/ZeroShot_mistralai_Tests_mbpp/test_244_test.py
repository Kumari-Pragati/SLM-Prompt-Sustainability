import unittest
from mbpp_244_code import next_Perfect_Square

class TestNextPerfectSquare(unittest.TestCase):

    def test_next_perfect_square_positive(self):
        self.assertEqual(next_Perfect_Square(4), 9)
        self.assertEqual(next_Perfect_Square(25), 36)
        self.assertEqual(next_Perfect_Square(36), 49)
        self.assertEqual(next_Perfect_Square(225), 289)
        self.assertEqual(next_Perfect_Square(625), 729)

    def test_next_perfect_square_zero(self):
        self.assertEqual(next_Perfect_Square(0), 1)

    def test_next_perfect_square_negative(self):
        self.assertEqual(next_Perfect_Square(-1), 1)
        self.assertEqual(next_Perfect_Square(-4), 1)
        self.assertEqual(next_Perfect_Square(-25), 49)
        self.assertEqual(next_Perfect_Square(-225), 289)
        self.assertEqual(next_Perfect_Square(-625), 729)
