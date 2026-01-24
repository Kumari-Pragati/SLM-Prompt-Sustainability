import unittest
from mbpp_497_code import surfacearea_cone

class TestSurfaceAreaCone(unittest.TestCase):

    def test_simple_input(self):
        self.assertEqual(surfacearea_cone(1, 2), 15.707963267948966)
        self.assertEqual(surfacearea_cone(2, 3), 38.48520617663035)

    def test_edge_input(self):
        self.assertEqual(surfacearea_cone(0, 1), 0)
        self.assertEqual(surfacearea_cone(1, 0), math.pi)
        self.assertEqual(surfacearea_cone(1, math.sqrt(2)), 13.065629647753104)

    def test_boundary_input(self):
        self.assertEqual(surfacearea_cone(math.pi, math.pi), math.pi * (math.pi * 2 + math.sqrt(math.pi * math.pi + math.pi * math.pi)))
        self.assertEqual(surfacearea_cone(math.sqrt(2), math.sqrt(3)), 2 * math.sqrt(2) * (math.sqrt(2) + math.sqrt(2 + math.sqrt(2))))
