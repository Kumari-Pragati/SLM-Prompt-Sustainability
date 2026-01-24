import unittest
from mbpp_244_code import next_Perfect_Square

class TestNextPerfectSquare(unittest.TestCase):
    def test_typical_cases(self):
        self.assertEqual(next_Perfect_Square(4), 9)
        self.assertEqual(next_Perfect_Square(25), 36)
        self.assertEqual(next_Perfect_Square(36), 49)
        self.assertEqual(next_Perfect_Square(225), 289)

    def test_edge_and_boundary_cases(self):
        self.assertEqual(next_Perfect_Square(0), 1)
        self.assertEqual(next_Perfect_Square(1), 4)
        self.assertEqual(next_Perfect_Square(16), 25)
        self.assertEqual(next_Perfect_Square(288), 324)
        self.assertEqual(next_Perfect_Square(289), 441)
        self.assertEqual(next_Perfect_Square(296), 361)
