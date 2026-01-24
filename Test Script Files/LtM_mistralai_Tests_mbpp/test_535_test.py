import unittest
from mbpp_535_code import topbottom_surfacearea

class TestTopBottomSurfaceArea(unittest.TestCase):
    def test_simple_positive(self):
        self.assertEqual(topbottom_surfacearea(1), 3.141592653589793)

    def test_typical_positive(self):
        self.assertEqual(topbottom_surfacearea(5), 78.53981633974483)

    def test_edge_zero(self):
        self.assertEqual(topbottom_surfacearea(0), 0)

    def test_edge_negative(self):
        self.assertAlmostEqual(topbottom_surfacearea(-1), -3.141592653589793)

    def test_edge_large_positive(self):
        self.assertAlmostEqual(topbottom_surfacearea(1e6), 3.141592653589793e8)
