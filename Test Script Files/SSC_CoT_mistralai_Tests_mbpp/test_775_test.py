import unittest
from mbpp_775_code import odd_position

class TestOddPosition(unittest.TestCase):
    def test_normal(self):
        self.assertTrue(odd_position([1, 3, 5, 7, 9]))
        self.assertTrue(odd_position([2, 4, 6, 8, 10]))

    def test_edge_cases(self):
        self.assertTrue(odd_position([]))
        self.assertTrue(odd_position([1]))
        self.assertTrue(odd_position([2, 2, 2, 2, 2]))
        self.assertTrue(odd_position([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))

    def test_boundary(self):
        self.assertTrue(odd_position([0, 1, 2]))
        self.assertTrue(odd_position([-1, 0, 1]))

    def test_invalid_inputs(self):
        self.assertFalse(odd_position([0, 0, 0]))
        self.assertFalse(odd_position([1.5, 3, 5]))
        self.assertRaises(TypeError, odd_position, [1, 2, "3"])
