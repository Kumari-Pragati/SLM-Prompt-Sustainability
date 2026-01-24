import unittest
from mbpp_630_code import Iterable

class TestGetCoordinates(unittest.TestCase):

    def test_empty_input(self):
        self.assertListEqual(get_coordinates((0,)), [])

    def test_single_element(self):
        self.assertListEqual(get_coordinates((1,)), [0])

    def test_multiple_elements(self):
        self.assertListEqual(get_coordinates((2, 3)), [0, 1, 2])

    def test_negative_elements(self):
        self.assertListEqual(get_coordinates((-1, 2)), [-1])
        self.assertListEqual(get_coordinates((-2, -3)), [-2, -1, 0])

    def test_zero_elements(self):
        self.assertListEqual(get_coordinates((0, 0)), [])

    def test_large_positive_elements(self):
        self.assertListEqual(get_coordinates((100, 200)), [98, 99, 100, 101])

    def test_large_negative_elements(self):
        self.assertListEqual(get_coordinates((-100, -200)), [-101, -100, -99, -98])

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            get_coordinates(123)
        with self.assertRaises(TypeError):
            get_coordinates(('a', 'b'))
        with self.assertRaises(TypeError):
            get_coordinates([1, 2, 3])
