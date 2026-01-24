import unittest
from mbpp_312_code import volume_cone

class TestVolumeCone(unittest.TestCase):

    def test_typical_inputs(self):
        self.assertAlmostEqual(volume_cone(1, 2), 3.14159265359, places=5)

    def test_edge_cases(self):
        self.assertAlmostEqual(volume_cone(0, 0), 0)
        self.assertAlmostEqual(volume_cone(0, 1), 0)
        self.assertAlmostEqual(volume_cone(1, 0), 0)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            volume_cone('a', 2)
        with self.assertRaises(TypeError):
            volume_cone(1, 'b')

    def test_boundary_conditions(self):
        self.assertAlmostEqual(volume_cone(1, 1), 0.5235987755982988, places=5)
        self.assertAlmostEqual(volume_cone(2, 2), 12.566370614359172, places=5)
