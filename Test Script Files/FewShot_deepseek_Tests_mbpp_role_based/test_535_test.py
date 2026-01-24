import unittest
from mbpp_535_code import topbottom_surfacearea

class TestTopBottomSurfaceArea(unittest.TestCase):
    def test_typical_case(self):
        self.assertAlmostEqual(topbottom_surfacearea(5), 3.1415 * 5 * 5)

    def test_boundary_conditions(self):
        self.assertAlmostEqual(topbottom_surfacearea(0), 0)
        self.assertAlmostEqual(topbottom_surfacearea(1), 3.1415)

    def test_edge_cases(self):
        self.assertAlmostEqual(topbottom_surfacearea(10), 3.1415 * 10 * 10)
        self.assertAlmostEqual(topbottom_surfacearea(100), 3.1415 * 100 * 100)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            topbottom_surfacearea("5")
        with self.assertRaises(ValueError):
            topbottom_surfacearea(-5)
