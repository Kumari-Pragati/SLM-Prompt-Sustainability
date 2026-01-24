import unittest
from mbpp_812_code import road_rd

class TestRoadRd(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(road_rd('123 Main Road'), '123 Main Rd.')

    def test_edge_case_no_match(self):
        self.assertEqual(road_rd('123 Main'), '123 Main')

    def test_edge_case_match_at_start(self):
        self.assertEqual(road_rd('Road 123'), 'Rd. 123')

    def test_edge_case_match_at_end(self):
        self.assertEqual(road_rd('123 Road'), '123 Rd.')

    def test_edge_case_match_at_start_and_end(self):
        self.assertEqual(road_rd('Road Road'), 'Rd. Rd.')

    def test_invalid_input_non_string(self):
        with self.assertRaises(TypeError):
            road_rd(123)
