import unittest
from mbpp_82_code import volume_sphere

class TestVolumeSphere(unittest.TestCase):

    def test_simple_input(self):
        self.assertAlmostEqual(volume_sphere(1), 4.188790204786391)

    def test_edge_input(self):
        self.assertAlmostEqual(volume_sphere(0), 0)
        self.assertAlmostEqual(volume_sphere(1e100), 4.98715147670e307)

    def test_negative_input(self):
        self.assertAlmostEqual(volume_sphere(-1), -4.188790204786391)

    def test_complex_input(self):
        self.assertAlmostEqual(volume_sphere(2.5), 20.61562496280776)
