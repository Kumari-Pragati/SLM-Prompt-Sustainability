import unittest
from mbpp_85_code import surfacearea_sphere

class TestSurfaceAreaSphere(unittest.TestCase):
    def test_typical_case(self):
        self.assertAlmostEqual(surfacearea_sphere(5), 78.53981633974483)

    def test_edge_case(self):
        self.assertAlmostEqual(surfacearea_sphere(0), 0)

    def test_edge_case(self):
        self.assertAlmostEqual(surfacearea_sphere(1), 12.566370614359172)

    def test_edge_case(self):
        self.assertAlmostEqual(surfacearea_sphere(-1), 12.566370614359172)

    def test_edge_case(self):
        self.assertAlmostEqual(surfacearea_sphere(10), 314.1592653589793)

    def test_edge_case(self):
        self.assertAlmostEqual(surfacearea_sphere(-10), 314.1592653589793)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            surfacearea_sphere("five")
