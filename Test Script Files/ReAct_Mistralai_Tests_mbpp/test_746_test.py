import unittest
from mbpp_746_code import sector_area

class TestSectorArea(unittest.TestCase):

    def setUp(self):
        self.pi = 22 / 7

    def test_sector_area_positive(self):
        # Typical case: valid input within range
        result = sector_area(3, 90)
        self.assertEqual(result, 28.316227766016837)

    def test_sector_area_zero_angle(self):
        # Edge case: angle equals 0
        result = sector_area(2, 0)
        self.assertEqual(result, 0)

    def test_sector_area_full_circle(self):
        # Edge case: angle equals 360
        result = sector_area(1, 360)
        self.assertEqual(result, None)

    def test_sector_area_negative_radius(self):
        # Error case: negative radius
        with self.assertRaises(ValueError):
            sector_area(-1, 180)

    def test_sector_area_zero_radius(self):
        # Error case: zero radius
        with self.assertRaises(ValueError):
            sector_area(0, 180)

    def test_sector_area_angle_greater_than_360(self):
        # Error case: angle greater than 360
        with self.assertRaises(ValueError):
            sector_area(1, 380)
