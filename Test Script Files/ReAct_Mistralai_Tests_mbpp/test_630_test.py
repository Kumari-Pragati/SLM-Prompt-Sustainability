import unittest
from mbpp_630_code import get_coordinates

class TestGetCoordinates(unittest.TestCase):

    def test_empty_list(self):
        self.assertListEqual(get_coordinates((0,)), [])

    def test_single_element_list(self):
        self.assertListEqual(get_coordinates((1,)), [0])

    def test_multiple_elements_list(self):
        self.assertListEqual(get_coordinates((2, 3, 4)), [0, 1, 2, 0, 1])

    def test_negative_elements_list(self):
        self.assertListEqual(get_coordinates((-1, 0, 1)), [-1, 0])

    def test_zero_elements_list(self):
        self.assertListEqual(get_coordinates((0, 0)), [])

    def test_large_elements_list(self):
        self.assertListEqual(get_coordinates((100, 100, 100)), list(range(100)))

    def test_negative_and_positive_elements_list(self):
        self.assertListEqual(get_coordinates((-2, 0, 3)), [-2, 0, 1, -2])

    def test_empty_sublist(self):
        self.assertListEqual(get_coordinates((0, sub=[1, 2, 3])), [1, 2, 3])
