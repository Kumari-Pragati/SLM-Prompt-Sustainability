import unittest
from mbpp_731_code import lateralsurface_cone

class TestLateralsurfaceCone(unittest.TestCase):

    def test_typical_inputs(self):
        self.assertAlmostEqual(lateralsurface_cone(5, 10), 78.53981633974483)

    def test_edge_cases(self):
        self.assertAlmostEqual(lateralsurface_cone(0, 0), 0)
        self.assertAlmostEqual(lateralsurface_cone(0, 10), 0)
        self.assertAlmostEqual(lateralsurface_cone(5, 0), 0)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            lateralsurface_cone('a', 10)
        with self.assertRaises(TypeError):
            lateralsurface_cone(5, 'b')

    def test_boundary_conditions(self):
        self.assertAlmostEqual(lateralsurface_cone(10, 10), 628.3185307179586)
        self.assertAlmostEqual(lateralsurface_cone(10, 0), 0)
