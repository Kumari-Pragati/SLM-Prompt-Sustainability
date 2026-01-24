import unittest
from mbpp_82_code import pi
from your_module import volume_sphere  # replace 'your_module' with the actual module name where the function is defined

class TestVolumeSphere(unittest.TestCase):

    def test_zero_radius(self):
        with self.assertRaises(ValueError):
            volume_sphere(0)

    def test_positive_radius(self):
        self.assertAlmostEqual(volume_sphere(1), 4.188790204786391, delta=0.001)
        self.assertAlmostEqual(volume_sphere(2), 133.1209032259887, delta=0.01)

    def test_negative_radius(self):
        with self.assertRaises(ValueError):
            volume_sphere(-1)
