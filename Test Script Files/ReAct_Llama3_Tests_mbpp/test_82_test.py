import unittest
from mbpp_82_code import volume_sphere

class TestVolumeSphere(unittest.TestCase):

    def test_typical_case(self):
        self.assertAlmostEqual(volume_sphere(1), (4/3)*math.pi)

    def test_edge_case_zero_radius(self):
        self.assertEqual(volume_sphere(0), 0)

    def test_edge_case_negative_radius(self):
        with self.assertRaises(OverflowError):
            volume_sphere(-1)

    def test_edge_case_zero_volume(self):
        self.assertAlmostEqual(volume_sphere(0.1), 0)

    def test_edge_case_large_radius(self):
        self.assertAlmostEqual(volume_sphere(10), (4/3)*math.pi*10**3)

    def test_edge_case_non_numeric_radius(self):
        with self.assertRaises(TypeError):
            volume_sphere('a')
