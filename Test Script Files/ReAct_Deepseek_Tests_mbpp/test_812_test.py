import unittest
from mbpp_812_code import road_rd

class TestRoadRd(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(road_rd('MainStreet'), 'MainStreet')
        self.assertEqual(road_rd('ParkWay'), 'ParkWay')

    def test_edge_case_with_suffix(self):
        self.assertEqual(road_rd('BakerRoad'), 'BakerRd.')

    def test_edge_case_without_suffix(self):
        self.assertEqual(road_rd('Highway'), 'Highway')

    def test_explicitly_handled_error_case(self):
        self.assertEqual(road_rd(''), '')
