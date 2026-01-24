import unittest
from mbpp_630_code import get_coordinates

class TestGetCoordinates(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(get_coordinates((1, 2, 3)), [[0, 1, 2], [0, 1, 3], [0, 2, 3], [1, 0, 2], [1, 0, 3], [1, 1, 3], [2, 0, 1], [2, 0, 2], [2, 1, 2]])

    def test_single_element(self):
        self.assertEqual(get_coordinates((1,)), [[0]])

    def test_empty_tuple(self):
        self.assertEqual(get_coordinates(()), [[]])

    def test_negative_elements(self):
        self.assertEqual(get_coordinates((-1, -2, -3)), [[-1, -1, -2], [-1, -1, -3], [-1, -2, -3], [-2, -1, -2], [-2, -1, -3], [-2, -2, -3], [-3, -1, -1], [-3, -1, -2], [-3, -2, -2]])

    def test_large_elements(self):
        self.assertEqual(get_coordinates((10, 20, 30)), [[9, 19, 29], [9, 19, 30], [9, 20, 30], [10, 9, 20], [10, 9, 30], [10, 10, 30], [20, 9, 10], [20, 9, 20], [20, 10, 20]])

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            get_coordinates("1, 2, 3")
