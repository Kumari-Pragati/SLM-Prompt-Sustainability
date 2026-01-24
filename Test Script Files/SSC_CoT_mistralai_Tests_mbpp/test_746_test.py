import unittest
from mbpp_746_code import sector_area

class TestSectorArea(unittest.TestCase):
    def test_normal_input(self):
        self.assertAlmostEqual(sector_area(3, 90), 28.274333882308138)
        self.assertAlmostEqual(sector_area(5, 180), 78.53981633974483)

    def test_edge_and_boundary_conditions(self):
        self.assertIsNone(sector_area(1, 361))
        self.assertAlmostEqual(sector_area(0, 360), 0)
        self.assertAlmostEqual(sector_area(1000, 360), 283495.0)

    def test_invalid_inputs(self):
        self.assertIsNone(sector_area(-1, 360))
        self.assertIsNone(sector_area(1, -359))
        self.assertIsNone(sector_area(0, 0))
        self.assertIsNone(sector_area(None, 360))
        self.assertIsNone(sector_area(3, "string"))
