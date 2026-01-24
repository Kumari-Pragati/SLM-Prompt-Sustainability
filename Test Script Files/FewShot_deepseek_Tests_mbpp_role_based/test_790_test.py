import unittest
from mbpp_790_code import even_position

class TestEvenPosition(unittest.TestCase):
    def test_typical_case(self):
        self.assertTrue(even_position([0, 1, 2, 3]))

    def test_edge_case(self):
        self.assertTrue(even_position([0]))
        self.assertFalse(even_position([1]))

    def test_boundary_case(self):
        self.assertTrue(even_position([0, 2]))
        self.assertFalse(even_position([1, 2]))

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            even_position(None)
        with self.assertRaises(TypeError):
            even_position('123')
        with self.assertRaises(TypeError):
            even_position(123)
