import unittest
from mbpp_92_code import is_undulating

class TestIsUndulating(unittest.TestCase):
    def test_typical_undulating(self):
        self.assertTrue(is_undulating("ababab"))

    def test_typical_non_undulating(self):
        self.assertFalse(is_undulating("abc"))

    def test_edge_undulating(self):
        self.assertTrue(is_undulating("abab"))

    def test_edge_non_undulating(self):
        self.assertFalse(is_undulating("a"))

    def test_boundary_undulating(self):
        self.assertTrue(is_undulating("abababab"))

    def test_boundary_non_undulating(self):
        self.assertFalse(is_undulating("a"))

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            is_undulating(123)

    def test_invalid_input_empty(self):
        with self.assertRaises(TypeError):
            is_undulating("")
