import unittest
from mbpp_630_code import get_coordinates

class TestGetCoordinates(unittest.TestCase):
    def test_typical_input(self):
        self.assertEqual(get_coordinates((2, 3)), [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)])

    def test_edge_case(self):
        self.assertEqual(get_coordinates((1, 1)), [(0, 0), (0, 1), (1, 0), (1, 1)])

    def test_edge_case2(self):
        self.assertEqual(get_coordinates((0, 1)), [(0, 0), (0, 1)])

    def test_edge_case3(self):
        self.assertEqual(get_coordinates((1, 0)), [(0, 0), (0, 1)])

    def test_edge_case4(self):
        self.assertEqual(get_coordinates((0, 0)), [(0, 0)])

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            get_coordinates("invalid input")

    def test_invalid_input2(self):
        with self.assertRaises(TypeError):
            get_coordinates([1, 2, 3])
