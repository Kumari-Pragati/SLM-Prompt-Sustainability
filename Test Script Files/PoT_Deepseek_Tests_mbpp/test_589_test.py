import unittest
from mbpp_589_code import perfect_squares

class TestPerfectSquares(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(perfect_squares(1, 10), [1, 4, 9])
        self.assertEqual(perfect_squares(25, 30), [25, 36])

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(perfect_squares(0, 10), [0, 1, 4, 9])
        self.assertEqual(perfect_squares(1, 1), [1])
        self.assertEqual(perfect_squares(100, 100), [])

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            perfect_squares("1", 10)
        with self.assertRaises(TypeError):
            perfect_squares(1, "10")
        with self.assertRaises(TypeError):
            perfect_squares("1", "10")
        with self.assertRaises(ValueError):
            perfect_squares(10, 1)
