import unittest
from mbpp_303_code import solve

class TestSolve(unittest.TestCase):
    def test_typical_case(self):
        self.assertTrue(solve([1, 2, 3, 4, 5], 5))

    def test_edge_case(self):
        self.assertTrue(solve([5, 4, 3, 2, 1], 5))

    def test_boundary_case(self):
        self.assertTrue(solve([1], 1))
        self.assertFalse(solve([5, 4, 3, 2, 1, 6], 6))

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            solve("1, 2, 3, 4, 5", 5)
        with self.assertRaises(TypeError):
            solve([1, 2, 3, 4, 5], "5")
        with self.assertRaises(TypeError):
            solve("1, 2, 3, 4, 5", "5")
