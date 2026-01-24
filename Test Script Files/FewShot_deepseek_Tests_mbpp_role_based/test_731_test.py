import unittest
from mbpp_731_code import lateralsurface_cone

class TestLatersurfaceCone(unittest.TestCase):
    def test_typical_case(self):
        self.assertAlmostEqual(lateralsurface_cone(3, 4), 37.6817, places=4)

    def test_boundary_conditions(self):
        self.assertEqual(lateralsurface_cone(0, 0), 0)
        self.assertEqual(lateralsurface_cone(0, 10), 0)
        self.assertEqual(lateralsurface_cone(10, 0), 0)

    def test_edge_cases(self):
        self.assertAlmostEqual(lateralsurface_cone(1, 1), 3.1416, places=4)
        self.assertAlmostEqual(lateralsurface_cone(10, 10), 314.1593, places=4)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            lateralsurface_cone("3", 4)
        with self.assertRaises(TypeError):
            lateralsurface_cone(3, "4")
        with self.assertRaises(TypeError):
            lateralsurface_cone("3", "4")
