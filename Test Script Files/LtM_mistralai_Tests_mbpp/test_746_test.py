import unittest
from mbpp_746_code import sector_area

class TestSectorArea(unittest.TestCase):

    def test_simple_input(self):
        self.assertAlmostEqual(sector_area(1, 90), 2.51)
        self.assertAlmostEqual(sector_area(2, 180), 12.57)

    def test_edge_and_boundary(self):
        self.assertIsNone(sector_area(1, 361))
        self.assertAlmostEqual(sector_area(0, 360), 0)
        self.assertAlmostEqual(sector_area(1, 0), 0)
        self.assertAlmostEqual(sector_area(1, 180.01), 12.57)
        self.assertAlmostEqual(sector_area(1, -90), 12.57)

    def test_complex_scenarios(self):
        self.assertAlmostEqual(sector_area(1, 540), None)
        self.assertAlmostEqual(sector_area(1, 720), None)
        self.assertAlmostEqual(sector_area(1, 900), None)
        self.assertAlmostEqual(sector_area(0.5, 360), 0)
        self.assertAlmostEqual(sector_area(10, 360), 706.54)
