import unittest
from mbpp_535_code import topbottom_surfacearea

class TestTopBottomSurfaceArea(unittest.TestCase):
    def test_positive_integer(self):
        self.assertEqual(topbottom_surfacearea(5), 78.53981633974483)
        self.assertEqual(topbottom_surfacearea(10), 314.1592653589793)

    def test_zero(self):
        self.assertEqual(topbottom_surfacearea(0), 0)

    def test_negative_number(self):
        self.assertRaises(ValueError, topbottom_surfacearea, -5)

    def test_float(self):
        self.assertAlmostEqual(topbottom_surfacearea(3.14), 9.999999999999999)

    def test_non_numeric(self):
        self.assertRaises(TypeError, topbottom_surfacearea, 'not a number')
