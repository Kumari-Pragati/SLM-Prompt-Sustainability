import unittest
from mbpp_746_code import sector_area

class TestSectorArea(unittest.TestCase):

    def test_sector_area_valid_input(self):
        self.assertAlmostEqual(sector_area(3, 90), 28.314285714285714)
        self.assertAlmostEqual(sector_area(4, 180), 20.106122486846704)
        self.assertAlmostEqual(sector_area(5, 360), 785.3981633974483)

    def test_sector_area_zero_radius(self):
        self.assertIsNone(sector_area(0, 90))

    def test_sector_area_negative_radius(self):
        self.assertIsNone(sector_area(-1, 90))

    def test_sector_area_negative_angle(self):
        self.assertIsNone(sector_area(3, -90))

    def test_sector_area_angle_greater_than_360(self):
        self.assertIsNone(sector_area(3, 400))
