import unittest
from mbpp_848_code import area_trapezium

class TestAreaTrapezium(unittest.TestCase):

    def test_typical_case(self):
        self.assertAlmostEqual(area_trapezium(5, 10, 7), 47.5)

    def test_edge_case_zero_height(self):
        self.assertEqual(area_trapezium(5, 10, 0), 0)

    def test_boundary_case_zero_bases(self):
        self.assertEqual(area_trapezium(0, 0, 10), 0)

    def test_corner_case_equal_bases(self):
        self.assertEqual(area_trapezium(5, 5, 10), 25)

    def test_negative_bases(self):
        with self.assertRaises(Exception):
            area_trapezium(-5, 10, 7)

    def test_negative_height(self):
        with self.assertRaises(Exception):
            area_trapezium(5, 10, -7)
