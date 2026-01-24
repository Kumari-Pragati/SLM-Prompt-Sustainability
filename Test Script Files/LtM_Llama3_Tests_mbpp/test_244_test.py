import unittest
from mbpp_244_code import next_Perfect_Square

class TestNextPerfectSquare(unittest.TestCase):
    def test_simple_inputs(self):
        self.assertEqual(next_Perfect_Square(1), 1)
        self.assertEqual(next_Perfect_Square(4), 4)
        self.assertEqual(next_Perfect_Square(9), 9)
        self.assertEqual(next_Perfect_Square(16), 16)
        self.assertEqual(next_Perfect_Square(25), 25)
        self.assertEqual(next_Perfect_Square(36), 36)
        self.assertEqual(next_Perfect_Square(49), 49)
        self.assertEqual(next_Perfect_Square(64), 64)
        self.assertEqual(next_Perfect_Square(81), 81)
        self.assertEqual(next_Perfect_Square(100), 100)

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(next_Perfect_Square(0), 0)
        self.assertEqual(next_Perfect_Square(1), 1)
        self.assertEqual(next_Perfect_Square(2), 1)
        self.assertEqual(next_Perfect_Square(3), 1)
        self.assertEqual(next_Perfect_Square(4), 2)
        self.assertEqual(next_Perfect_Square(5), 2)
        self.assertEqual(next_Perfect_Square(6), 4)
        self.assertEqual(next_Perfect_Square(7), 4)
        self.assertEqual(next_Perfect_Square(8), 4)
        self.assertEqual(next_Perfect_Square(9), 9)

    def test_more_complex_and_corner_cases(self):
        self.assertEqual(next_Perfect_Square(10), 5)
        self.assertEqual(next_Perfect_Square(11), 5)
        self.assertEqual(next_Perfect_Square(12), 9)
        self.assertEqual(next_Perfect_Square(13), 9)
        self.assertEqual(next_Perfect_Square(14), 9)
        self.assertEqual(next_Perfect_Square(15), 4)
        self.assertEqual(next_Perfect_Square(16), 4)
        self.assertEqual(next_Perfect_Square(17), 5)
        self.assertEqual(next_Perfect_Square(18), 9)
        self.assertEqual(next_Perfect_Square(19), 5)
        self.assertEqual(next_Perfect_Square(20), 5)
