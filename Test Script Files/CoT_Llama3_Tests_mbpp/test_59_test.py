import unittest
from mbpp_59_code import is_octagonal

class TestIsOctagonal(unittest.TestCase):
    def test_typical_cases(self):
        self.assertTrue(is_octagonal(1) == 1)
        self.assertTrue(is_octagonal(2) == 5)
        self.assertTrue(is_octagonal(3) == 19)

    def test_edge_cases(self):
        self.assertTrue(is_octagonal(0) == 0)
        self.assertTrue(is_octagonal(-1) == None)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            is_octagonal("a")
        with self.assertRaises(TypeError):
            is_octagonal(None)

    def test_boundary_cases(self):
        self.assertTrue(is_octagonal(10) == 277)
        self.assertTrue(is_octagonal(-10) == None)
