import unittest
from mbpp_812_code import road_rd

class TestRoadRd(unittest.TestCase):
    def test_normal_input(self):
        self.assertEqual(road_rd('123 Main Road'), '123 Main Rd.')
        self.assertEqual(road_rd('Avenue Road'), 'Avenue Rd.')
        self.assertEqual(road_rd('456 Elm Street Road'), '456 Elm Street Rd.')

    def test_edge_cases(self):
        self.assertEqual(road_rd(''), '')
        self.assertEqual(road_rd('123'), '123')
        self.assertEqual(road_rd('123 Main'), '123 Main')
        self.assertEqual(road_rd('Main Road 123'), 'Main Rd. 123')
        self.assertEqual(road_rd('123 Road'), '123 Rd.')
        self.assertEqual(road_rd('Road 123'), 'Rd. 123')

    def test_invalid_input(self):
        self.assertRaises(ValueError, road_rd, '123 Main$')
        self.assertRaises(ValueError, road_rd, '123 Main#')
        self.assertRaises(ValueError, road_rd, '123 Main%')
