import unittest
from mbpp_497_code import surfacearea_cone

class TestSurfaceAreaCones(unittest.TestCase):
    def test_simple_inputs(self):
        self.assertAlmostEqual(surfacearea_cone(1, 2), 3.14159265359)
        self.assertAlmostEqual(surfacearea_cone(2, 3), 12.5663706144)

    def test_edge_cases(self):
        self.assertAlmostEqual(surfacearea_cone(0, 0), 0)
        self.assertAlmostEqual(surfacearea_cone(0, 1), 0)
        self.assertAlmostEqual(surfacearea_cone(1, 0), 0)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            surfacearea_cone('a', 2)
        with self.assertRaises(TypeError):
            surfacearea_cone(1, 'b')
