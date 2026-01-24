import unittest
from mbpp_746_code import sector_area

class TestSectorArea(unittest.TestCase):

    def test_sector_area_with_valid_input(self):
        self.assertAlmostEqual(sector_area(5, 90), 19.63495436420765, places=5)
        self.assertAlmostEqual(sector_area(10, 180), 314.1592653589793, places=5)

    def test_sector_area_with_invalid_input(self):
        self.assertIsNone(sector_area(5, 360))
        self.assertIsNone(sector_area(5, 361))

    def test_sector_area_with_zero_input(self):
        self.assertEqual(sector_area(0, 90), 0)
        self.assertEqual(sector_area(0, 0), 0)

    def test_sector_area_with_negative_input(self):
        self.assertIsNone(sector_area(-5, 90))
        self.assertIsNone(sector_area(5, -90))
