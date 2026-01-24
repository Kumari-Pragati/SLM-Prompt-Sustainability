import unittest
from mbpp_812_code import road_rd

class TestRoadRd(unittest.TestCase):
    def test_simple_inputs(self):
        self.assertEqual(road_rd('Main Road'), 'Main Rd.')
        self.assertEqual(road_rd('Secondary Road'), 'Secondary Rd.')
        self.assertEqual(road_rd('Tertiary Road'), 'Tertiary Rd.')

    def test_edge_cases(self):
        self.assertEqual(road_rd(''), '')
        self.assertEqual(road_rd('Rd.'), 'Rd.')
        self.assertEqual(road_rd('Road'), 'Rd.')

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            road_rd(123)
        with self.assertRaises(TypeError):
            road_rd(None)
