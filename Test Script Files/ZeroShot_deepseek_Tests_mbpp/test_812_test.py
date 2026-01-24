import unittest
from mbpp_812_code import road_rd

class TestRoadRd(unittest.TestCase):

    def test_road_rd(self):
        self.assertEqual(road_rd('MainStreet'), 'MainStreet')
        self.assertEqual(road_rd('BakerRoad'), 'BakerRd.')
        self.assertEqual(road_rd('MapleRoad'), 'MapleRd.')
        self.assertEqual(road_rd('Parkway'), 'Parkway')
        self.assertEqual(road_rd('HighwayRoad'), 'HighwayRd.')
