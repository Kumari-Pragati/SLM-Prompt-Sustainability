import unittest
from mbpp_303_code import solve

class TestSolve(unittest.TestCase):
    def test_true(self):
        self.assertTrue(solve([1, 2, 3, 4, 5], 5))

    def test_false(self):
        self.assertFalse(solve([5, 4, 3, 2, 1], 5))

    def test_edge_case(self):
        self.assertTrue(solve([1, 1, 1, 1, 1], 5))

    def test_edge_case2(self):
        self.assertFalse(solve([5, 5, 5, 5, 5], 5))

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            solve("abc", 5)

    def test_invalid_input2(self):
        with self.assertRaises(TypeError):
            solve([1, 2, 3], "abc")
