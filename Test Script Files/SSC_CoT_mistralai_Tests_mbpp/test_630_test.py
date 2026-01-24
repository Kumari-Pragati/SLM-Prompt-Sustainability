import unittest
from mbpp_630_code import range
from six.moves import zip

from 630_code import get_coordinates

class TestGetCoordinates(unittest.TestCase):

    def test_normal_input(self):
        self.assertListEqual(get_coordinates((3, (1, 2))), [(2, 1), (2, 2), (2, 3)])
        self.assertListEqual(get_coordinates((3, (2, 2))), [(1, 2), (2, 2), (3, 2)])
        self.assertListEqual(get_coordinates((3, (3, 2))), [(2, 2), (3, 2), (4, 2)])

    def test_edge_and_boundary_conditions(self):
        self.assertListEqual(get_coordinates((1, (1, 1))), [(0, 1), (1, 1)])
        self.assertListEqual(get_coordinates((1, (1, 2))), [(0, 2), (1, 2)])
        self.assertListEqual(get_coordinates((1, (1, 3))), [(0, 3)])
        self.assertListEqual(get_coordinates((2, (2, 2))), [(1, 1), (1, 2), (1, 3), (2, 2)])

    def test_negative_input(self):
        self.assertRaises(ValueError, get_coordinates, ((-1, 1), (1, 2)))
        self.assertRaises(ValueError, get_coordinates, ((1, -1), (1, 2)))
        self.assertRaises(ValueError, get_coordinates, ((-1, -1), (1, 2)))
