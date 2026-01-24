import unittest
from mbpp_82_code import volume_sphere

class TestVolumeSphere(unittest.TestCase):

    def test_volume_sphere(self):
        self.assertAlmostEqual(volume_sphere(1), (4/3)*math.pi)
        self.assertAlmostEqual(volume_sphere(2), (4/3)*math.pi*2**3)
        self.assertAlmostEqual(volume_sphere(3), (4/3)*math.pi*3**3)
        self.assertAlmostEqual(volume_sphere(0), 0)
        self.assertAlmostEqual(volume_sphere(-1), 0)
        self.assertAlmostEqual(volume_sphere(-2), 0)
        self.assertAlmostEqual(volume_sphere(-3), 0)
