import unittest
from mbpp_812_code import road_rd

class TestRoadRd(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(road_rd('123 Main Road'), '123 Main Rd.')
        self.assertEqual(road_rd('Main Road'), 'Main Rd.')
        self.assertEqual(road_rd('123 45th Street Road'), '123 45th Street Rd.')

    def test_edge_case(self):
        self.assertEqual(road_rd(''), '')
        self.assertEqual(road_rd('123'), '123')
        self.assertEqual(road_rd('123 Main'), '123 Main')
        self.assertEqual(road_rd('Road'), 'Rd.')
        self.assertEqual(road_rd('123 Road 45'), '123 Road 45')
