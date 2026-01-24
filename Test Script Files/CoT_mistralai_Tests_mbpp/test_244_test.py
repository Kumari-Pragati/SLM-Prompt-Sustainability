import unittest
from mbpp_244_code import next_Perfect_Square

class TestNextPerfectSquare(unittest.TestCase):
    def test_perfect_square(self):
        self.assertEqual(next_Perfect_Square(4), 9)
        self.assertEqual(next_Perfect_Square(9), 16)
        self.assertEqual(next_Perfect_Square(16), 25)
        self.assertEqual(next_Perfect_Square(25), 36)

    def test_edge_cases(self):
        self.assertEqual(next_Perfect_Square(0), 1)
        self.assertEqual(next_Perfect_Square(1), 4)
        self.assertEqual(next_Perfect_Square(2), 4)
        self.assertEqual(next_Perfect_Square(3), 9)

    def test_invalid_inputs(self):
        self.assertRaises(TypeError, next_Perfect_Square, 'string')
        self.assertRaises(TypeError, next_Perfect_Square, -1)
        self.assertRaises(TypeError, next_Perfect_Square, float('nan'))
