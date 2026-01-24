import unittest
from mbpp_581_code import surface_Area

class TestSurfaceArea(unittest.TestCase):
    def test_positive_values(self):
        self.assertEqual(surface_Area(5, 3), 62)

    def test_zero_values(self):
        self.assertEqual(surface_Area(0, 0), 0)

    def test_negative_values(self):
        self.assertEqual(surface_Area(-5, 3), 30)

    def test_zero_base(self):
        self.assertEqual(surface_Area(0, 5), 10)

    def test_zero_side(self):
        self.assertEqual(surface_Area(5, 0), 10)

    def test_invalid_input_type(self):
        with self.assertRaises(TypeError):
            surface_Area('a', 3)

    def test_invalid_input_type2(self):
        with self.assertRaises(TypeError):
            surface_Area(5, 'b')
