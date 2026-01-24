import unittest
from mbpp_746_code import sector_area

class TestSectorArea(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(sector_area(3, 90), 28.274333882308138)
        self.assertEqual(sector_area(2, 180), 12.566370614359172)
        self.assertEqual(sector_area(4, 270), 33.958333333333336)

    def test_edge_case(self):
        self.assertEqual(sector_area(1, 360), None)
        self.assertEqual(sector_area(0, 360), None)
        self.assertEqual(sector_area(1, 0), None)

    def test_boundary_case(self):
        self.assertEqual(sector_area(1, 359), 358.71433882308138)
        self.assertEqual(sector_area(1, 359.9), 358.71433882308138)
        self.assertEqual(sector_area(1, 359.99), 358.71433882308138)
        self.assertEqual(sector_area(1, 360.01), None)
