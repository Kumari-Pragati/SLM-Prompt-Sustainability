import unittest
from mbpp_535_code import topbottom_surfacearea

class TestTopbottomSurfacearea(unittest.TestCase):
    def test_typical_input(self):
        self.assertEqual(topbottom_surfacearea(5), 78.53981633974483)

    def test_edge_case_zero(self):
        self.assertEqual(topbottom_surfacearea(0), 0)

    def test_edge_case_negative(self):
        with self.assertRaises(TypeError):
            topbottom_surfacearea(-1)

    def test_edge_case_non_numeric(self):
        with self.assertRaises(TypeError):
            topbottom_surfacearea('a')

    def test_edge_case_large_input(self):
        self.assertEqual(topbottom_surfacearea(100), 31415.0)
