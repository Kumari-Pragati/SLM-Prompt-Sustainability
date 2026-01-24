import unittest
from mbpp_746_code import sector_area

class TestSectorArea(unittest.TestCase):
    def test_simple_valid_input(self):
        self.assertEqual(sector_area(5, 90), 78.57142857142857)

    def test_edge_case_a_360(self):
        self.assertIsNone(sector_area(5, 360))

    def test_edge_case_a_0(self):
        self.assertIsNone(sector_area(5, 0))

    def test_edge_case_r_0(self):
        self.assertEqual(sector_area(0, 90), 0)

    def test_edge_case_r_negative(self):
        with self.assertRaises(TypeError):
            sector_area(-5, 90)

    def test_edge_case_a_negative(self):
        with self.assertRaises(TypeError):
            sector_area(5, -90)

    def test_edge_case_r_and_a_negative(self):
        with self.assertRaises(TypeError):
            sector_area(-5, -90)

    def test_edge_case_r_and_a_zero(self):
        with self.assertRaises(ZeroDivisionError):
            sector_area(0, 0)

    def test_edge_case_a_greater_than_360(self):
        self.assertIsNone(sector_area(5, 361))

    def test_edge_case_r_greater_than_100(self):
        self.assertEqual(sector_area(101, 90), 1111.4285714285714)

    def test_edge_case_a_greater_than_100(self):
        self.assertEqual(sector_area(5, 101), 1111.4285714285714)

    def test_edge_case_r_and_a_greater_than_100(self):
        self.assertEqual(sector_area(101, 101), 1111.4285714285714)
