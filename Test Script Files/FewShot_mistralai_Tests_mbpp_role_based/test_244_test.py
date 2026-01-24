import unittest
from mbpp_244_code import next_Perfect_Square

class TestNextPerfectSquare(unittest.TestCase):
    def test_perfect_square(self):
        self.assertEqual(next_Perfect_Square(16), 25)
        self.assertEqual(next_Perfect_Square(25), 36)
        self.assertEqual(next_Perfect_Square(36), 49)

    def test_edge_case_sqrt(self):
        self.assertEqual(next_Perfect_Square(2), 4)
        self.assertEqual(next_Perfect_Square(9), 16)
        self.assertEqual(next_Perfect_Square(22), 49)

    def test_edge_case_sqrt_plus_one(self):
        self.assertEqual(next_Perfect_Square(4), 9)
        self.assertEqual(next_Perfect_Square(10), 25)
        self.assertEqual(next_Perfect_Square(21), 49)

    def test_negative_number(self):
        self.assertRaises(ValueError, next_Perfect_Square, -1)

    def test_zero(self):
        self.assertRaises(ValueError, next_Perfect_Square, 0)
