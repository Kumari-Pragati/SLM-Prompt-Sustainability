import unittest
from mbpp_812_code import road_rd

class TestRoadRd(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(road_rd('123 Main Road'), '123 Main Rd.')
        self.assertEqual(road_rd('123 Elm Street Road'), '123 Elm Street Rd.')
        self.assertEqual(road_rd('123 First Avenue Road'), '123 First Avenue Rd.')

    def test_edge_case_no_space_before_road(self):
        self.assertEqual(road_rd('123MainRoad'), '123Main Rd.')
        self.assertEqual(road_rd('123ElmStreetRoad'), '123Elm Street Rd.')
        self.assertEqual(road_rd('123FirstAvenueRoad'), '123First Avenue Rd.')

    def test_edge_case_no_road(self):
        self.assertEqual(road_rd('123 Main'), '123 Main')
        self.assertEqual(road_rd('123 Elm Street'), '123 Elm Street')
        self.assertEqual(road_rd('123 First Avenue'), '123 First Avenue')

    def test_edge_case_multiple_words_after_road(self):
        self.assertEqual(road_rd('123 Main Road A'), '123 Main Road A')
        self.assertEqual(road_rd('123 Elm Street Road B'), '123 Elm Street Road B')
        self.assertEqual(road_rd('123 First Avenue Road C'), '123 First Avenue Road C')

    def test_edge_case_no_period(self):
        self.assertEqual(road_rd('123 Main Road.'), '123 Main Road.')
        self.assertEqual(road_rd('123 Elm Street Road.'), '123 Elm Street Road.')
        self.assertEqual(road_rd('123 First Avenue Road.'), '123 First Avenue Road.')
