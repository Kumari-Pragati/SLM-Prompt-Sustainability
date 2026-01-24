import unittest
from mbpp_574_code import surfacearea_cylinder

class TestSurfaceAreaCylinder(unittest.TestCase):

    def test_surface_area_cylinder(self):
        self.assertAlmostEqual(surfacearea_cylinder(1,1), 6.283185307179586)
        self.assertAlmostEqual(surfacearea_cylinder(2,2), 12.566370614359172)
        self.assertAlmostEqual(surfacearea_cylinder(3,3), 18.84955637777778)
        self.assertAlmostEqual(surfacearea_cylinder(4,4), 25.13274122871835)
        self.assertAlmostEqual(surfacearea_cylinder(5,5), 31.41592653589793)

    def test_surface_area_cylinder_invalid_input(self):
        with self.assertRaises(TypeError):
            surfacearea_cylinder('a', 1)
        with self.assertRaises(TypeError):
            surfacearea_cylinder(1, 'b')
