import unittest
from mbpp_574_code import surfacearea_cylinder

class TestSurfaceAreaCylinder(unittest.TestCase):
    def test_typical_case(self):
        self.assertAlmostEqual(surfacearea_cylinder(2, 5), 62.83*2 + 62.83*10)

    def test_boundary_conditions(self):
        self.assertAlmostEqual(surfacearea_cylinder(0, 0), 0)
        self.assertAlmostEqual(surfacearea_cylinder(1, 0), 2*3.1415*1*1)
        self.assertAlmostEqual(surfacearea_cylinder(0, 1), 2*3.1415*0*1)

    def test_edge_cases(self):
        self.assertAlmostEqual(surfacearea_cylinder(1, 1000), 2*3.1415*1*1000 + 2*3.1415*1*1000)
        self.assertAlmostEqual(surfacearea_cylinder(1000, 1), 2*3.1415*1000*1000 + 2*3.1415*1000*1)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            surfacearea_cylinder("2", 5)
        with self.assertRaises(TypeError):
            surfacearea_cylinder(2, "5")
        with self.assertRaises(TypeError):
            surfacearea_cylinder("2", "5")
        with self.assertRaises(ValueError):
            surfacearea_cylinder(-2, 5)
        with self.assertRaises(ValueError):
            surfacearea_cylinder(2, -5)
