import unittest
from mbpp_14_code import find_Volume

class TestFindVolume(unittest.TestCase):

    def test_find_volume_positive(self):
        self.assertEqual(find_Volume(3, 4, 5), 60.0)
        self.assertEqual(find_Volume(2, 2, 2), 12.0)
        self.assertEqual(find_Volume(1, 1, 1), 1.0 / 2)

    def test_find_volume_zero(self):
        self.assertAlmostEqual(find_Volume(0, 4, 5), 0.0)
        self.assertAlmostEqual(find_Volume(3, 0, 5), 0.0)
        self.assertAlmostEqual(find_Volume(3, 4, 0), 0.0)

    def test_find_volume_negative(self):
        self.assertAlmostEqual(find_Volume(-3, 4, 5), 0.0)
        self.assertAlmostEqual(find_Volume(3, -4, 5), 0.0)
        self.assertAlmostEqual(find_Volume(3, 4, -5), 0.0)
