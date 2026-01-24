import unittest
from mbpp_535_code import topbottom_surfacearea

class TestTopbottomSurfacearea(unittest.TestCase):
    def test_typical_case(self):
        self.assertAlmostEqual(topbottom_surfacearea(5), 78.53981633974483)

    def test_edge_case(self):
        self.assertAlmostEqual(topbottom_surfacearea(0), 0)

    def test_edge_case(self):
        self.assertAlmostEqual(topbottom_surfacearea(1), 3.1415)

    def test_edge_case(self):
        self.assertAlmostEqual(topbottom_surfacearea(-1), 3.1415)

    def test_edge_case(self):
        self.assertAlmostEqual(topbottom_surfacearea(10), 314.1592653589793)

    def test_edge_case(self):
        self.assertAlmostEqual(topbottom_surfacearea(-10), 314.1592653589793)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            topbottom_surfacearea('a')
