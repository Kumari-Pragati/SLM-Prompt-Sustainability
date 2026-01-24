import unittest
from mbpp_497_code import surfacearea_cone

class TestSurfaceAreaCone(unittest.TestCase):

    def test_typical_case(self):
        self.assertAlmostEqual(surfacearea_cone(3, 5), 84.77989103172124)

    def test_edge_case(self):
        self.assertAlmostEqual(surfacearea_cone(0, 0), 0)

    def test_boundary_case(self):
        self.assertAlmostEqual(surfacearea_cone(1, 1), 3.141592653589793)

    def test_large_numbers(self):
        self.assertAlmostEqual(surfacearea_cone(100, 200), 12566.370614359171)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            surfacearea_cone("3", 5)

        with self.assertRaises(TypeError):
            surfacearea_cone(3, "5")

        with self.assertRaises(TypeError):
            surfacearea_cone("3", "5")

        with self.assertRaises(ValueError):
            surfacearea_cone(-3, 5)

        with self.assertRaises(ValueError):
            surfacearea_cone(3, -5)

        with self.assertRaises(ValueError):
            surfacearea_cone(-3, -5)
