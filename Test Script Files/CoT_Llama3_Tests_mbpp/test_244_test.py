import unittest
from mbpp_244_code import next_Perfect_Square

class TestNextPerfectSquare(unittest.TestCase):

    def test_typical_inputs(self):
        self.assertEqual(next_Perfect_Square(16), 25)
        self.assertEqual(next_Perfect_Square(25), 36)
        self.assertEqual(next_Perfect_Square(36), 49)

    def test_edge_cases(self):
        self.assertEqual(next_Perfect_Square(0), 1)
        self.assertEqual(next_Perfect_Square(1), 4)
        self.assertEqual(next_Perfect_Square(4), 9)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            next_Perfect_Square('a')
        with self.assertRaises(TypeError):
            next_Perfect_Square(None)

    def test_boundary_conditions(self):
        self.assertEqual(next_Perfect_Square(100), 121)
        self.assertEqual(next_Perfect_Square(121), 144)
