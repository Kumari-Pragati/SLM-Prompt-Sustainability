import unittest
from mbpp_82_code import volume_sphere

class TestVolumeSphere(unittest.TestCase):
    def test_typical_case(self):
        self.assertAlmostEqual(volume_sphere(3), 268.09488733898305)

    def test_edge_case_zero(self):
        self.assertEqual(volume_sphere(0), 0)

    def test_edge_case_one(self):
        self.assertAlmostEqual(volume_sphere(1), 4.188790204786391)

    def test_edge_case_negative(self):
        self.assertEqual(volume_sphere(-1), math.nan)

    def test_corner_case_integer(self):
        self.assertAlmostEqual(volume_sphere(2), 20.10658678777778)
