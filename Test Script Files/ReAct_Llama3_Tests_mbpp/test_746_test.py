import unittest
from mbpp_746_code import sector_area

class TestSectorArea(unittest.TestCase):
    def test_valid_sector_area(self):
        self.assertAlmostEqual(sector_area(5, 90), 78.57142857142857)

    def test_invalid_angle(self):
        self.assertIsNone(sector_area(5, 400))

    def test_zero_radius(self):
        self.assertIsNone(sector_area(0, 90))

    def test_zero_angle(self):
        self.assertEqual(sector_area(5, 0), 0)

    def test_invalid_radius(self):
        with self.assertRaises(TypeError):
            sector_area('five', 90)

    def test_invalid_angle_type(self):
        with self.assertRaises(TypeError):
            sector_area(5, 'ninety')
