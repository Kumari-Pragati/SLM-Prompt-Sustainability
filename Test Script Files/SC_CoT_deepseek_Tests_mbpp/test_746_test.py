import unittest
from mbpp_746_code import sector_area

class TestSectorArea(unittest.TestCase):

    def test_typical_case(self):
        self.assertAlmostEqual(sector_area(5, 90), 19.634954, places=5)

    def test_typical_case_2(self):
        self.assertAlmostEqual(sector_area(10, 180), 314.159265, places=5)

    def test_boundary_case(self):
        self.assertAlmostEqual(sector_area(1, 360), 3.14159265, places=5)

    def test_edge_case(self):
        self.assertIsNone(sector_area(1, 361))

    def test_invalid_input_case(self):
        with self.assertRaises(TypeError):
            sector_area('5', 90)

        with self.assertRaises(TypeError):
            sector_area(5, '90')

        with self.assertRaises(TypeError):
            sector_area('5', '90')

        with self.assertRaises(ValueError):
            sector_area(5, -90)
