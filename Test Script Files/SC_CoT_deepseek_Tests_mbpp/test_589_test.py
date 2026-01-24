import unittest
from mbpp_589_code import perfect_squares

class TestPerfectSquares(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(perfect_squares(1, 25), [1, 4, 9, 16, 25])

    def test_boundary_conditions(self):
        self.assertEqual(perfect_squares(1, 1), [1])
        self.assertEqual(perfect_squares(0, 0), [])

    def test_edge_cases(self):
        self.assertEqual(perfect_squares(30, 40), [])
        self.assertEqual(perfect_squares(100, 1000), [144, 169, 196, 225, 256, 289, 324, 361, 400, 441, 484, 529, 576, 625, 676, 729, 784, 841, 900])

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            perfect_squares("1", 2)
        with self.assertRaises(TypeError):
            perfect_squares(1, "2")
        with self.assertRaises(TypeError):
            perfect_squares("1", "2")
        with self.assertRaises(ValueError):
            perfect_squares(-1, 2)
        with self.assertRaises(ValueError):
            perfect_squares(2, -1)
