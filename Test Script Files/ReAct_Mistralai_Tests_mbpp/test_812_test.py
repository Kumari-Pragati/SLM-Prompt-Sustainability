import unittest
from mbpp_812_code import road_rd

class TestRoadRd(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(road_rd('123 Main Road'), '123 Main Rd.')

    def test_edge_case_no_space_before_road(self):
        self.assertEqual(road_rd('123MainRoad'), '123Main Rd.')

    def test_edge_case_no_space_after_road(self):
        self.assertEqual(road_rd('123 Main Road '), '123 Main Rd. ')

    def test_edge_case_only_road(self):
        self.assertEqual(road_rd('Road'), 'Rd.')

    def test_edge_case_multiple_roads(self):
        self.assertEqual(road_rd('123 First Road Second Road'), '123 First Rd. Second Rd.')

    def test_error_case_non_string(self):
        with self.assertRaises(TypeError):
            road_rd(123)
