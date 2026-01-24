import unittest
from mbpp_244_code import next_Perfect_Square

class TestNextPerfectSquare(unittest.TestCase):

    def test_simple_perfect_square(self):
        self.assertEqual(next_Perfect_Square(4), 9)
        self.assertEqual(next_Perfect_Square(9), 16)
        self.assertEqual(next_Perfect_Square(16), 25)

    def test_edge_cases(self):
        self.assertEqual(next_Perfect_Square(0), 1)
        self.assertEqual(next_Perfect_Square(1), 4)
        self.assertEqual(next_Perfect_Square(2), 4)
        self.assertEqual(next_Perfect_Square(3), 4)
        self.assertEqual(next_Perfect_Square(256), 289)

    def test_non_perfect_square(self):
        self.assertEqual(next_Perfect_Square(5), 9)
        self.assertEqual(next_Perfect_Square(6), 9)
        self.assertEqual(next_Perfect_Square(7), 9)
        self.assertEqual(next_Perfect_Square(8), 25)
        self.assertEqual(next_Perfect_Square(22), 49)
