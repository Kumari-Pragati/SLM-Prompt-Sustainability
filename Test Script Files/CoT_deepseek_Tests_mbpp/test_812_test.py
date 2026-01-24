import unittest
from mbpp_812_code import road_rd

class TestRoadRd(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(road_rd('MainStreet'), 'MainStreet')
        self.assertEqual(road_rd('ParkWay'), 'ParkWay')

    def test_edge_case(self):
        self.assertEqual(road_rd('Road'), 'Rd.')

    def test_boundary_case(self):
        self.assertEqual(road_rd(''), '')

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            road_rd(123)
