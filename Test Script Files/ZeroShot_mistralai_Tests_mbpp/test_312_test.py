import unittest
from mbpp_312_code import volume_cone

class TestVolumeCone(unittest.TestCase):

    def test_volume_cone_positive(self):
        self.assertAlmostEqual(volume_cone(1, 2), 13.0 * math.pi / 3)
        self.assertAlmostEqual(volume_cone(2, 3), 36.0 * math.pi)
        self.assertAlmostEqual(volume_cone(3, 4), 106.0 * math.pi / 3)

    def test_volume_cone_zero(self):
        self.assertAlmostEqual(volume_cone(0, 1), 0)
        self.assertAlmostEqual(volume_cone(1, 0), 0)

    def test_volume_cone_negative(self):
        self.assertAlmostEqual(volume_cone(-1, 2), 13.0 * math.pi / 3)
        self.assertAlmostEqual(volume_cone(1, -2), -13.0 * math.pi / 3)
