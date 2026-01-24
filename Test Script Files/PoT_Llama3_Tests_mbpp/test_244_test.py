import unittest
from mbpp_244_code import next_Perfect_Square

class TestNextPerfectSquare(unittest.TestCase):
    def test_typical_cases(self):
        self.assertEqual(next_Perfect_Square(1), 1)
        self.assertEqual(next_Perfect_Square(4), 4)
        self.assertEqual(next_Perfect_Square(9), 16)
        self.assertEqual(next_Perfect_Square(16), 25)
        self.assertEqual(next_Perfect_Square(25), 25)
        self.assertEqual(next_Perfect_Square(36), 49)

    def test_edge_and_boundary_cases(self):
        self.assertEqual(next_Perfect_Square(0), 0)
        self.assertEqual(next_Perfect_Square(1), 1)
        self.assertEqual(next_Perfect_Square(2), 4)
        self.assertEqual(next_Perfect_Square(3), 4)
        self.assertEqual(next_Perfect_Square(4), 4)
        self.assertEqual(next_Perfect_Square(5), 9)

    def test_corner_cases(self):
        self.assertEqual(next_Perfect_Square(10), 16)
        self.assertEqual(next_Perfect_Square(11), 16)
        self.assertEqual(next_Perfect_Square(12), 16)
        self.assertEqual(next_Perfect_Square(13), 16)
        self.assertEqual(next_Perfect_Square(14), 16)
