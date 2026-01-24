import unittest
from mbpp_812_code import road_rd

class TestRoadRd(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(road_rd('123 Main Road'), '123 Main Rd.')
        self.assertEqual(road_rd('Main Road'), 'Main Rd.')
        self.assertEqual(road_rd('123 456 Main Road'), '123 456 Main Rd.')

    def test_edge_case_no_space(self):
        self.assertEqual(road_rd('MainRoad'), 'Main Rd.')
        self.assertEqual(road_rd('123MainRoad'), '123Main Rd.')

    def test_edge_case_no_road(self):
        self.assertEqual(road_rd('123 Main'), '123 Main')
        self.assertEqual(road_rd('Main'), 'Main')

    def test_edge_case_multiple_roads(self):
        self.assertEqual(road_rd('123 Main Roads'), '123 Main Roads')
        self.assertEqual(road_rd('123 Main Road Road'), '123 Main Road Rd.')

    def test_invalid_input(self):
        self.assertRaises(TypeError, road_rd, 123)
        self.assertRaises(TypeError, road_rd, [1, 2, 3])
        self.assertRaises(TypeError, road_rd, (1, 2, 3))
        self.assertRaises(TypeError, road_rd, None)
        self.assertRaises(TypeError, road_rd, {})
