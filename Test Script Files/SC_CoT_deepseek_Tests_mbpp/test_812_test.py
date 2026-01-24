import unittest
from mbpp_812_code import road_rd

class TestRoadRd(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(road_rd('MainStreet'), 'MainStreet')
        self.assertEqual(road_rd('Park Avenue'), 'Park Avenue')

    def test_edge_cases(self):
        self.assertEqual(road_rd(''), '')
        self.assertEqual(road_rd('Road'), 'Rd.')
        self.assertEqual(road_rd('Street Road'), 'Street Rd.')
        self.assertEqual(road_rd('Street Road '), 'Street Rd.')

    def test_corner_cases(self):
        self.assertEqual(road_rd('Road Road'), 'Road Rd.')
        self.assertEqual(road_rd('Road Road '), 'Road Rd.')
        self.assertEqual(road_rd(' Road'), ' Rd.')
        self.assertEqual(road_rd(' Road '), ' Rd.')

    def test_invalid_inputs(self):
        # The function does not handle invalid inputs, so this test will raise an error if the function is not implemented correctly.
        with self.assertRaises(TypeError):
            road_rd(123)
