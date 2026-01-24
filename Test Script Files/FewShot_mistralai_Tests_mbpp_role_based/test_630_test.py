import unittest
from mbpp_630_code import get_coordinates

class TestGetCoordinates(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(get_coordinates(()), [])

    def test_single_element(self):
        self.assertEqual(get_coordinates((1,)), [[0], [1], [2]])

    def test_multiple_elements(self):
        self.assertEqual(get_coordinates((1, 2)), [[0], [1], [2], [0, 1], [0, 2], [1, 2]])

    def test_negative_elements(self):
        self.assertEqual(get_coordinates((-1, 2)), [[-2], [-1], [0], [-1], [-2]])

    def test_zero_elements(self):
        self.assertEqual(get_coordinates((0, 2)), [[-1], [0], [1]])

    def test_out_of_range_elements(self):
        self.assertEqual(get_coordinates((3, 2)), [])
