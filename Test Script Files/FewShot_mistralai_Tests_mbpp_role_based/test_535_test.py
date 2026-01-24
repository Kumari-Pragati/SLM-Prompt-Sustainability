import unittest
from mbpp_535_code import topbottom_surfacearea

class TestTopBottomSurfaceArea(unittest.TestCase):
    def test_positive_number(self):
        self.assertEqual(topbottom_surfacearea(3), 28.274333882308138)

    def test_zero(self):
        self.assertEqual(topbottom_surfacearea(0), 0)

    def test_negative_number(self):
        with self.assertRaises(ValueError):
            topbottom_surfacearea(-1)

    def test_non_numeric_input(self):
        with self.assertRaises(TypeError):
            topbottom_surfacearea('not a number')
