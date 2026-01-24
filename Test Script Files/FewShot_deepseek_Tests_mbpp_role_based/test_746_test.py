import unittest
from mbpp_746_code import sector_area

class TestSectorArea(unittest.TestCase):
    def test_typical_case(self):
        self.assertAlmostEqual(sector_area(5, 90), 19.63495436423841, places=5)

    def test_boundary_case(self):
        self.assertEqual(sector_area(0, 90), 0)

    def test_edge_case(self):
        self.assertEqual(sector_area(10, 360), 100*22/7)

    def test_invalid_input(self):
        self.assertIsNone(sector_area(5, 360))
        self.assertIsNone(sector_area(-5, 90))
        self.assertIsNone(sector_area(5, -90))
