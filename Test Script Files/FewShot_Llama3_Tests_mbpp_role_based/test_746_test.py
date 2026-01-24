import unittest
from mbpp_746_code import sector_area

class TestSectorArea(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertAlmostEqual(sector_area(10, 90), 78.57142857142857)

    def test_edge_case_a_360(self):
        self.assertIsNone(sector_area(10, 360))

    def test_edge_case_a_0(self):
        self.assertIsNone(sector_area(10, 0))

    def test_edge_case_r_0(self):
        self.assertIsNone(sector_area(0, 90))

    def test_invalid_input_type(self):
        with self.assertRaises(TypeError):
            sector_area("10", 90)

    def test_invalid_input_type_2(self):
        with self.assertRaises(TypeError):
            sector_area(10, "90")
