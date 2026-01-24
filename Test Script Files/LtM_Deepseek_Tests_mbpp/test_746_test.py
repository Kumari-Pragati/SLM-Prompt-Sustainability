import unittest
from mbpp_746_code import sector_area

class TestSectorArea(unittest.TestCase):

    def test_typical_case(self):
        self.assertAlmostEqual(sector_area(5, 90), 19.6349540649, places=5)

    def test_full_circle(self):
        self.assertIsNone(sector_area(5, 360))

    def test_zero_angle(self):
        self.assertEqual(sector_area(5, 0), 0)

    def test_negative_angle(self):
        self.assertIsNone(sector_area(5, -10))

    def test_large_angle(self):
        self.assertIsNone(sector_area(5, 400))

    def test_zero_radius(self):
        self.assertEqual(sector_area(0, 90), 0)

    def test_negative_radius(self):
        self.assertIsNone(sector_area(-5, 90))

    def test_large_radius(self):
        self.assertAlmostEqual(sector_area(10000, 90), 785398163.3, places=5)
