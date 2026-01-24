import unittest
from mbpp_535_code import topbottom_surfacearea

class TestTopBottomSurfaceArea(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(topbottom_surfacearea(2), 12.566360605520874)

    def test_edge_case_zero(self):
        self.assertEqual(topbottom_surfacearea(0), 0)

    def test_edge_case_negative(self):
        self.assertAlmostEqual(topbottom_surfacearea(-1), -3.141592653589793)

    def test_edge_case_large_number(self):
        self.assertAlmostEqual(topbottom_surfacearea(1e6), 3.141592653589793e7)
