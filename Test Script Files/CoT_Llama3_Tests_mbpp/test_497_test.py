import unittest
from mbpp_497_code import surfacearea_cone

class TestSurfaceAreaCones(unittest.TestCase):

    def test_typical_inputs(self):
        self.assertAlmostEqual(surfacearea_cone(5, 10), 3.141592653589793*5*15, places=10)

    def test_edge_cases(self):
        self.assertAlmostEqual(surfacearea_cone(0, 10), 0, places=10)
        self.assertAlmostEqual(surfacearea_cone(5, 0), 0, places=10)
        self.assertAlmostEqual(surfacearea_cone(0, 0), 0, places=10)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            surfacearea_cone('a', 10)
        with self.assertRaises(TypeError):
            surfacearea_cone(5, 'b')

    def test_boundary_conditions(self):
        self.assertAlmostEqual(surfacearea_cone(10, 10), 3.141592653589793*10*20, places=10)
        self.assertAlmostEqual(surfacearea_cone(10, 0), 0, places=10)
