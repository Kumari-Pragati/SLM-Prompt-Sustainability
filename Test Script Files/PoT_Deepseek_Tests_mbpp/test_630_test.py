import unittest
from mbpp_630_code import get_coordinates

class TestGetCoordinates(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(get_coordinates([1, 2]), [[0, 1, 2], [0, 1, 2]])

    def test_edge_case(self):
        self.assertEqual(get_coordinates([0]), [[-1, 0, 1]])

    def test_boundary_case(self):
        self.assertEqual(get_coordinates([2, 3]), [[-1, 0, 1], [-1, 0, 1], [-1, 0, 1], [-1, 0, 1], [-1, 0, 1], [-1, 0, 1], [-1, 0, 1], [-1, 0, 1], [-1, 0, 1], [-1, 0, 2]])

    def test_invalid_input(self):
        with self.assertRaises(Exception):
            get_coordinates([])
