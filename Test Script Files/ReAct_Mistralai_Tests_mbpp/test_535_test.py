import unittest
from mbpp_535_code import topbottom_surfacearea

class TestTopBottomSurfaceArea(unittest.TestCase):

    def test_positive_normal_case(self):
        "Test topbottom_surfacearea with a positive normal case"
        result = topbottom_surfacearea(5)
        self.assertEqual(result, 78.53981633974483)

    def test_zero_case(self):
        "Test topbottom_surfacearea with zero"
        result = topbottom_surfacearea(0)
        self.assertEqual(result, 0)

    def test_negative_case(self):
        "Test topbottom_surfacearea with a negative number"
        with self.assertRaises(ValueError):
            topbottom_surfacearea(-1)

    def test_float_case(self):
        "Test topbottom_surfacearea with a float number"
        result = topbottom_surfacearea(3.14)
        self.assertAlmostEqual(result, 9.999999999999999)

    def test_large_number_case(self):
        "Test topbottom_surfacearea with a large number"
        result = topbottom_surfacearea(1e10)
        self.assertEqual(result, 3.141592653589793e22)
