import unittest
from mbpp_746_code import sector_area

class TestSectorArea(unittest.TestCase):
    def test_positive_r_and_a(self):
        self.assertAlmostEqual(sector_area(3, 90), 28.353)

    def test_zero_r_and_a(self):
        self.assertEqual(sector_area(0, 90), 0)

    def test_negative_r_and_a(self):
        self.assertIsNone(sector_area(-1, 90))

    def test_large_angle(self):
        self.assertIsNone(sector_area(3, 361))

    def test_angle_greater_than_360(self):
        self.assertIsNone(sector_area(3, 721))
