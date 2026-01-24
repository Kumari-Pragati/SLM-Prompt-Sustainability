import unittest
from mbpp_775_code import odd_position

class TestOddPosition(unittest.TestCase):
    def test_typical_case(self):
        self.assertTrue(odd_position([1, 3, 5]))

    def test_boundary_condition(self):
        self.assertTrue(odd_position([0]))
        self.assertFalse(odd_position([1]))

    def test_edge_case(self):
        self.assertTrue(odd_position([]))
        self.assertFalse(odd_position([1, 2]))

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            odd_position(123)
        with self.assertRaises(TypeError):
            odd_position('123')
