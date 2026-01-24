import unittest
from mbpp_812_code import road_rd

class TestRoadRd(unittest.TestCase):
    def test_typical(self):
        self.assertEqual(road_rd('123 Main Road'), '123 Main Rd.')
        self.assertEqual(road_rd('456 Elm Street'), '456 Elm St.')
        self.assertEqual(road_rd('789 Oak Avenue'), '789 Oak Ave.')

    def test_edge(self):
        self.assertEqual(road_rd('123 Main'), '123 Main')
        self.assertEqual(road_rd('456 Elm'), '456 Elm')

    def test_boundary(self):
        self.assertEqual(road_rd('123 Main Roadway'), '123 Main Rdway')
        self.assertEqual(road_rd('456 Elm Streetway'), '456 Elm Stway')

    def test_invalid(self):
        with self.assertRaises(TypeError):
            road_rd(123)
        with self.assertRaises(TypeError):
            road_rd(None)
