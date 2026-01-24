import unittest
from mbpp_630_code import get_coordinates

class TestGetCoordinates(unittest.TestCase):
    def test_empty_input(self):
        self.assertEqual(get_coordinates([]), [[]])

    def test_single_element(self):
        self.assertEqual(get_coordinates([1]), [[-1, 0, 1]])

    def test_multiple_elements(self):
        self.assertEqual(get_coordinates([1, 2]), [[-1, 0, 1], [-2, -1, 0, 1, 2], [-1, 0, 1, 2]])

    def test_large_input(self):
        self.assertEqual(get_coordinates([1, 2, 3]), [[-1, 0, 1], [-2, -1, 0, 1, 2], [-1, 0, 1, 2], 
                                                      [-2, -1, 0, 1, 2, 3], [-1, 0, 1, 2, 3], [0, 1, 2, 3]])
