import unittest
from mbpp_630_code import get_coordinates

class TestGetCoordinates(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(get_coordinates((1, 2)), [(0, 1, 2), (1, 1, 2), (2, 1, 2)])

    def test_edge_case_zero(self):
        self.assertEqual(get_coordinates((0, 2)), [(0, 2)])

    def test_edge_case_one(self):
        self.assertEqual(get_coordinates((1, 2)), [(0, 1, 2), (1, 1, 2), (2, 1, 2)])

    def test_edge_case_negative(self):
        with self.assertRaises(IndexError):
            get_coordinates((-1, 2))

    def test_invalid_input_type(self):
        with self.assertRaises(TypeError):
            get_coordinates("test")
