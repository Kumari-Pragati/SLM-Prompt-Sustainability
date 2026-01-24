import unittest
from mbpp_812_code import road_rd

class TestRoadRd(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(road_rd('Main Road'), 'Main Rd.')
        self.assertEqual(road_rd('Highway Road'), 'Highway Rd.')
        self.assertEqual(road_rd('Street Road'), 'Street Rd.')

    def test_edge_cases(self):
        self.assertEqual(road_rd(''), '')
        self.assertEqual(road_rd('Rd'), 'Rd')
        self.assertEqual(road_rd('Road.'), 'Rd.')
        self.assertEqual(road_rd('Road, Ave'), 'Rd, Ave')

    def test_complex(self):
        self.assertEqual(road_rd('123 Main Road'), '123 Main Rd.')
        self.assertEqual(road_rd('Main Road, Apt 4B'), 'Main Rd, Apt 4B')
        self.assertEqual(road_rd('Main Road, Apt 4B, New York, NY 10001'), 'Main Rd, Apt 4B, New York, NY 10001')
