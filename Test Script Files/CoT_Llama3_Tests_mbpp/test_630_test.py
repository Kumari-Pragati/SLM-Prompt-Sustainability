import unittest
from mbpp_630_code import get_coordinates

class TestGetCoordinates(unittest.TestCase):
    def test_get_coordinates_empty_tuple(self):
        self.assertEqual(get_coordinates(()), [])

    def test_get_coordinates_single_element(self):
        self.assertEqual(get_coordinates((1,)), [(1,)])

    def test_get_coordinates_multiple_elements(self):
        self.assertEqual(get_coordinates((2, 3)), [(1, 1), (1, 2), (1, 3), (2, 1), (2, 2), (2, 3)])

    def test_get_coordinates_nested_tuples(self):
        self.assertEqual(get_coordinates((1, (2, 3))), [(1, 1), (1, 2), (1, 3), (2, 1), (2, 2), (2, 3)])

    def test_get_coordinates_invalid_input(self):
        with self.assertRaises(TypeError):
            get_coordinates("invalid input")
