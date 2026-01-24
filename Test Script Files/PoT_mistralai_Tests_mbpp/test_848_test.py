import unittest
from mbpp_848_code import area_trapezium

class TestAreaTrapezium(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(area_trapezium(3, 4, 5), 15.0)

    def test_edge_case_zero_base(self):
        self.assertEqual(area_trapezium(0, 4, 5), 0.0)

    def test_edge_case_zero_height(self):
        self.assertEqual(area_trapezium(3, 4, 0), 0.0)

    def test_edge_case_negative_base(self):
        self.assertEqual(area_trapezium(-3, 4, 5), 0.0)

    def test_edge_case_negative_height(self):
        self.assertEqual(area_trapezium(3, -4, 5), 0.0)

    def test_corner_case_equal_bases(self):
        self.assertEqual(area_trapezium(4, 4, 5), 16.0)
