import unittest
from mbpp_775_code import odd_position

class TestOddPosition(unittest.TestCase):
    def test_simple(self):
        self.assertTrue(odd_position([1, 3, 5, 7]))
        self.assertFalse(odd_position([2, 4, 6, 8]))
        self.assertTrue(odd_position([1, 2, 3, 4]))
        self.assertFalse(odd_position([0, 1, 2, 3]))

    def test_edge_cases(self):
        self.assertTrue(odd_position([]))
        self.assertFalse(odd_position([1]))
        self.assertTrue(odd_position([1, 1, 1, 1]))
        self.assertFalse(odd_position([2, 2, 2, 2]))

    def test_complex(self):
        self.assertTrue(odd_position([1, 2, 3, 4, 5, 6, 7, 8, 9]))
        self.assertFalse(odd_position([0, 1, 2, 3, 4, 5, 6, 7, 8]))
        self.assertTrue(odd_position([1, 0, 1, 0, 1, 0, 1, 0, 1]))
        self.assertFalse(odd_position([2, 3, 2, 3, 2, 3, 2, 3, 2]))
