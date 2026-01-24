import unittest
from mbpp_312_code import volume_cone

class TestVolumeCone(unittest.TestCase):

    def test_typical_inputs(self):
        self.assertAlmostEqual(volume_cone(1, 2), 3.14159265359, places=5)

    def test_edge_cases(self):
        self.assertAlmostEqual(volume_cone(0, 2), 0, places=5)
        self.assertAlmostEqual(volume_cone(1, 0), 0, places=5)
        self.assertAlmostEqual(volume_cone(0, 0), 0, places=5)

    def test_negative_inputs(self):
        with self.assertRaises(TypeError):
            volume_cone(-1, 2)

        with self.assertRaises(TypeError):
            volume_cone(1, -2)

    def test_non_numeric_inputs(self):
        with self.assertRaises(TypeError):
            volume_cone('a', 2)

        with self.assertRaises(TypeError):
            volume_cone(1, 'b')

    def test_mixed_type_inputs(self):
        with self.assertRaises(TypeError):
            volume_cone(1, 'a')

        with self.assertRaises(TypeError):
            volume_cone('a', 2)
