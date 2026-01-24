import unittest
from mbpp_812_code import road_rd

class TestRoadRd(unittest.TestCase):
    def test_simple_case(self):
        self.assertEqual(road_rd('MainStreet'), 'MainStreet')
        self.assertEqual(road_rd('ParkWay'), 'ParkWay')

    def test_edge_cases(self):
        self.assertEqual(road_rd(''), '')
        self.assertEqual(road_rd('Road'), 'Rd.')
        self.assertEqual(road_rd('Street'), 'Street')

    def test_complex_cases(self):
        self.assertEqual(road_rd('1234 Road'), '1234 Rd.')
        self.assertEqual(road_rd('Mountain Boulevard'), 'Mountain Boulevard')
        self.assertEqual(road_rd('Pine Street Road'), 'Pine Street Rd.')
