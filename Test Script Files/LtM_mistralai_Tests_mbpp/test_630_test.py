import unittest
from mbpp_630_code import Iterable

class TestGetCoordinates(unittest.TestCase):

    def test_simple(self):
        self.assertListEqual(get_coordinates((1, 2)), [(0, 1), (1, 1), (2, 1)])
        self.assertListEqual(get_coordinates((3, 4)), [(2, 3), (3, 3), (4, 3), (2, 4), (3, 4), (4, 4)])

    def test_edge_and_boundary(self):
        self.assertListEqual(get_coordinates((0, 0)), [])
        self.assertListEqual(get_coordinates((0, 1)), [(0, 0)])
        self.assertListEqual(get_coordinates((1, 0)), [(1, 0)])
        self.assertListEqual(get_coordinates((1, -1)), [])
        self.assertListEqual(get_coordinates((-1, 1)), [(-1, 0)])

    def test_complex(self):
        self.assertListEqual(get_coordinates((5, 5)), list(range(5)) + list(range(5, -1, -1)))
        self.assertListEqual(get_coordinates((1, 2, 3)), [(1, 2), (2, 2), (3, 2), (1, 3), (2, 3), (3, 3)])

    def test_invalid_input(self):
        self.assertRaises(TypeError, get_coordinates, 1)
        self.assertRaises(TypeError, get_coordinates, (1,))
        self.assertRaises(TypeError, get_coordinates, (1, 2, 3, "a"))
