import unittest
from mbpp_497_code import surfacearea_cone

class TestSurfaceAreaCone(unittest.TestCase):

    def test_typical_case(self):
        self.assertAlmostEqual(surfacearea_cone(3, 4), 83.23926463327972)

    def test_zero_radius(self):
        self.assertEqual(surfacearea_cone(0, 5), 0)

    def test_zero_height(self):
        self.assertEqual(surfacearea_cone(3, 0), 0)

    def test_negative_radius(self):
        with self.assertRaises(ValueError):
            surfacearea_cone(-3, 4)

    def test_negative_height(self):
        with self.assertRaises(ValueError):
            surfacearea_cone(3, -4)

    def test_large_numbers(self):
        self.assertAlmostEqual(surfacearea_cone(1000, 2000), 62831853.07179586)
