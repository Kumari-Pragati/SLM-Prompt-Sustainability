import unittest
from mbpp_630_code import get_coordinates

class TestGetCoordinates(unittest.TestCase):

    def test_simple_input(self):
        self.assertEqual(get_coordinates([1, 2]), [[0, 1, 2]])

    def test_edge_conditions(self):
        self.assertEqual(get_coordinates([0]), [[-1, 0, 1]])
        self.assertEqual(get_coordinates([]), [[]])

    def test_complex_cases(self):
        self.assertEqual(get_coordinates([1, 2, 3]), [[-1, 0, 1], [-2, -1, 0, 1, 2], [-3, -2, -1, 0, 1, 2, 3]])
