import unittest
from mbpp_812_code import road_rd

class TestRoadRd(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(road_rd('MainStreet'), 'MainStreet')
        self.assertEqual(road_rd('ParkLane'), 'ParkLane')

    def test_edge_case(self):
        self.assertEqual(road_rd('1234 Road'), '1234 Rd.')
        self.assertEqual(road_rd('MountainViewRoad'), 'MountainViewRd.')

    def test_boundary_case(self):
        self.assertEqual(road_rd('Road'), 'Rd.')
        self.assertEqual(road_rd('Road123'), 'Rd.123')

    def test_corner_case(self):
        self.assertEqual(road_rd('RoadEnd'), 'Rd.End')
        self.assertEqual(road_rd('EndRoad'), 'EndRd.')
