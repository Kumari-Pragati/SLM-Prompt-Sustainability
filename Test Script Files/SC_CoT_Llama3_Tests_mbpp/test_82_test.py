import unittest
from mbpp_82_code import volume_sphere

class TestVolumeSphere(unittest.TestCase):
    def test_typical_input(self):
        self.assertAlmostEqual(volume_sphere(1), (4/3)*math.pi)

    def test_edge_case_zero(self):
        self.assertAlmostEqual(volume_sphere(0), 0)

    def test_edge_case_negative(self):
        with self.assertRaises(TypeError):
            volume_sphere(-1)

    def test_edge_case_zero_radius(self):
        self.assertAlmostEqual(volume_sphere(0), 0)

    def test_edge_case_negative_radius(self):
        with self.assertRaises(TypeError):
            volume_sphere(-1)

    def test_typical_input_large(self):
        self.assertAlmostEqual(volume_sphere(5), (4/3)*math.pi*5*5*5)

    def test_typical_input_small(self):
        self.assertAlmostEqual(volume_sphere(0.1), (4/3)*math.pi*0.1*0.1*0.1)
