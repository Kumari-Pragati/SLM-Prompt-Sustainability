import unittest
from mbpp_746_code import sector_area

class TestSectorArea(unittest.TestCase):
    def test_positive_values(self):
        self.assertAlmostEqual(sector_area(3, 90), 28.274333882308138)
        self.assertAlmostEqual(sector_area(2, 180), 12.566370614359172)
        self.assertAlmostEqual(sector_area(1, 360), 6.283185307179586)

    def test_zero_angle(self):
        self.assertEqual(sector_area(1, 0), 0)

    def test_negative_angle(self):
        self.assertIsNone(sector_area(1, -180))
        self.assertIsNone(sector_area(1, -360))

    def test_zero_radius(self):
        self.assertIsNone(sector_area(0, 90))

    def test_negative_radius(self):
        self.assertIsNone(sector_area(-1, 90))
