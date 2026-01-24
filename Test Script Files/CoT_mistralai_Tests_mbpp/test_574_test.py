import unittest
from mbpp_574_code import surfacearea_cylinder

class TestSurfaceAreaCylinder(unittest.TestCase):
    def test_positive_values(self):
        self.assertAlmostEqual(surfacearea_cylinder(2, 3), 154.13716476570951)
        self.assertAlmostEqual(surfacearea_cylinder(1, 10), 78.53981633974483)

    def test_zero_value(self):
        self.assertEqual(surfacearea_cylinder(0, 5), 0)
        self.assertEqual(surfacearea_cylinder(5, 0), 0)

    def test_negative_values(self):
        self.assertAlmostEqual(surfacearea_cylinder(-2, 3), 154.13716476570951)
        self.assertAlmostEqual(surfacearea_cylinder(2, -3), 154.13716476570951)

    def test_invalid_inputs(self):
        self.assertRaises(TypeError, surfacearea_cylinder, 'a', 3)
        self.assertRaises(TypeError, surfacearea_cylinder, 5, 'b')
