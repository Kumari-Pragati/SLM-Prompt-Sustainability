import unittest
from mbpp_535_code import topbottom_surfacearea

class TestTopbottomSurfacearea(unittest.TestCase):
    def test_typical_case(self):
        self.assertAlmostEqual(topbottom_surfacearea(5), 78.53981633974483)

    def test_edge_case(self):
        self.assertAlmostEqual(topbottom_surfacearea(0), 0)

    def test_edge_case_negative(self):
        with self.assertRaises(TypeError):
            topbottom_surfacearea(-5)

    def test_edge_case_zero(self):
        with self.assertRaises(TypeError):
            topbottom_surfacearea(0)

    def test_edge_case_non_numeric(self):
        with self.assertRaises(TypeError):
            topbottom_surfacearea('five')

    def test_edge_case_non_numeric_negative(self):
        with self.assertRaises(TypeError):
            topbottom_surfacearea(-'five')

    def test_edge_case_non_numeric_zero(self):
        with self.assertRaises(TypeError):
            topbottom_surfacearea(0)
