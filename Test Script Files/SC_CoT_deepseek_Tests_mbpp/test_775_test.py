import unittest
from mbpp_775_code import odd_position

class TestOddPosition(unittest.TestCase):
    def test_typical_case(self):
        self.assertTrue(odd_position([1, 3, 5]))

    def test_edge_case(self):
        self.assertTrue(odd_position([0]))
        self.assertFalse(odd_position([1]))

    def test_boundary_case(self):
        self.assertTrue(odd_position([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]))
        self.assertFalse(odd_position([0, 1, 2, 3, 4, 5, 6, 7, 8, 10]))

    def test_special_case(self):
        self.assertTrue(odd_position([2, 4, 6, 8, 10]))
        self.assertFalse(odd_position([1, 3, 5, 7, 9]))

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            odd_position(123)
        with self.assertRaises(TypeError):
            odd_position('123')
        with self.assertRaises(TypeError):
            odd_position(None)
