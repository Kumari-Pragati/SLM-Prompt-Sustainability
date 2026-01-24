import unittest
from mbpp_535_code import topbottom_surfacearea

class TestTopBottomSurfaceArea(unittest.TestCase):

    def test_typical_case(self):
        self.assertAlmostEqual(topbottom_surfacearea(5), 3.1415*5*5)

    def test_boundary_case(self):
        self.assertAlmostEqual(topbottom_surfacearea(0), 0)

    def test_edge_case(self):
        self.assertAlmostEqual(topbottom_surfacearea(1), 3.1415)

    def test_negative_input(self):
        with self.assertRaises(Exception):
            topbottom_surfacearea(-1)

    def test_non_numeric_input(self):
        with self.assertRaises(Exception):
            topbottom_surfacearea('a')
