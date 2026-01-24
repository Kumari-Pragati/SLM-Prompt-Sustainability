import unittest
from mbpp_244_code import next_Perfect_Square

class TestNextPerfectSquare(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(next_Perfect_Square(1), 4)
        self.assertEqual(next_Perfect_Square(4), 9)
        self.assertEqual(next_Perfect_Square(9), 16)
        self.assertEqual(next_Perfect_Square(16), 25)

    def test_edge_cases(self):
        self.assertEqual(next_Perfect_Square(0), 1)
        self.assertEqual(next_Perfect_Square(1), 4)
        self.assertEqual(next_Perfect_Square(2), 4)
        self.assertEqual(next_Perfect_Square(3), 4)
        self.assertEqual(next_Perfect_Square(4), 9)

    def test_boundary_conditions(self):
        self.assertEqual(next_Perfect_Square(10**18), 10**18 + 1)
        self.assertEqual(next_Perfect_Square(10**19), 10**19 + 1)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            next_Perfect_Square("1")
        with self.assertRaises(TypeError):
            next_Perfect_Square(None)
        with self.assertRaises(TypeError):
            next_Perfect_Square([])
        with self.assertRaises(TypeError):
            next_Perfect_Square({})
