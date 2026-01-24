import unittest
from mbpp_746_code import sector_area

class TestSectorArea(unittest.TestCase):

    def test_valid_sector_area(self):
        self.assertAlmostEqual(sector_area(5, 90), 78.57142857142857)

    def test_invalid_angle(self):
        self.assertIsNone(sector_area(5, 400))

    def test_zero_angle(self):
        self.assertIsNone(sector_area(5, 0))

    def test_zero_radius(self):
        self.assertIsNone(sector_area(0, 90))

    def test_negative_angle(self):
        with self.assertRaises(TypeError):
            sector_area(5, -10)

    def test_negative_radius(self):
        with self.assertRaises(TypeError):
            sector_area(-5, 90)

    def test_non_numeric_angle(self):
        with self.assertRaises(TypeError):
            sector_area(5, 'a')

    def test_non_numeric_radius(self):
        with self.assertRaises(TypeError):
            sector_area('a', 90)
