import unittest
from mbpp_574_code import surfacearea_cylinder

class TestSurfaceAreaCylinder(unittest.TestCase):
    def test_typical_case(self):
        self.assertAlmostEqual(surfacearea_cylinder(5, 10), 628.32)

    def test_edge_case(self):
        self.assertAlmostEqual(surfacearea_cylinder(0, 10), 62.83)

    def test_edge_case(self):
        self.assertAlmostEqual(surfacearea_cylinder(5, 0), 78.54)

    def test_edge_case(self):
        self.assertAlmostEqual(surfacearea_cylinder(0, 0), 0)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            surfacearea_cylinder('a', 10)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            surfacearea_cylinder(5, 'b')

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            surfacearea_cylinder('a', 'b')
