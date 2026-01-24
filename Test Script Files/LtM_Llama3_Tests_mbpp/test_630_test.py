import unittest
from mbpp_630_code import get_coordinates

class TestGetCoordinates(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(get_coordinates((1, 2)), [(1, 2)])
        self.assertEqual(get_coordinates((2, 1)), [(2, 1)])
        self.assertEqual(get_coordinates((1, 1)), [(1, 1)])

    def test_edge(self):
        self.assertEqual(get_coordinates((0, 1)), [(0, 1)])
        self.assertEqual(get_coordinates((1, 0)), [(1, 0)])
        self.assertEqual(get_coordinates((1, 1)), [(1, 1)])

    def test_max(self):
        self.assertEqual(get_coordinates((10, 10)), [(1, 1), (1, 2), (1, 3),..., (10, 9), (10, 10)])

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            get_coordinates("test")
