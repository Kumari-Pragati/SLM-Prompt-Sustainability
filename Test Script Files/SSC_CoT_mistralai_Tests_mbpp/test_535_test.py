import unittest
from mbpp_535_code import topbottom_surfacearea

class TestTopBottomSurfaceArea(unittest.TestCase):
    def test_normal_input(self):
        self.assertEqual(topbottom_surfacearea(5), 78.53981633974483)

    def test_edge_cases(self):
        self.assertEqual(topbottom_surfacearea(0), 0)
        self.assertEqual(topbottom_surfacearea(1e-5), 3.141515262287676e-10)
        self.assertEqual(topbottom_surfacearea(1e6), 3.141592653589793e12)

    def test_negative_input(self):
        self.assertRaises(ValueError, topbottom_surfacearea, -1)

    def test_non_numeric_input(self):
        self.assertRaises(TypeError, topbottom_surfacearea, 'not a number')
