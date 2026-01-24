import unittest
from mbpp_59_code import is_octagonal

class TestIsOctagonal(unittest.TestCase):
    def test_typical(self):
        self.assertTrue(is_octagonal(1))
        self.assertTrue(is_octagonal(2))
        self.assertTrue(is_octagonal(3))

    def test_edge(self):
        self.assertFalse(is_octagonal(0))
        self.assertFalse(is_octagonal(-1))

    def test_boundary(self):
        self.assertTrue(is_octagonal(4))
        self.assertTrue(is_octagonal(5))

    def test_corner(self):
        self.assertFalse(is_octagonal(-2))
