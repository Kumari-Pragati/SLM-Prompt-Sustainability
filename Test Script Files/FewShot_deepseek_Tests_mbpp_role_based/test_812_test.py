import unittest
from mbpp_812_code import road_rd

class TestRoadRd(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(road_rd('Main Street'), 'Main Street')
        self.assertEqual(road_rd('Maple Road'), 'Maple Rd.')

    def test_edge_case(self):
        self.assertEqual(road_rd('Park Avenue Road'), 'Park Avenue Rd.')

    def test_boundary_case(self):
        self.assertEqual(road_rd('Highway Road'), 'Highway Rd.')

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            road_rd(123)
