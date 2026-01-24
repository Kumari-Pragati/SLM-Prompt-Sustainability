import unittest
from mbpp_630_code import get_coordinates

class TestGetCoordinates(unittest.TestCase):
    def test_typical_use_case(self):
        test_tup = [1, 2, 3]
        expected_output = [[1, 2, 3], [0, 2, 3], [2, 2, 3], [1, 1, 3], [1, 3, 3], [1, 2, 2], [1, 2, 4]]
        self.assertEqual(get_coordinates(test_tup), expected_output)

    def test_edge_condition(self):
        test_tup = [0, 0, 0]
        expected_output = [[0, 0, 0], [-1, 0, 0], [1, 0, 0], [0, -1, 0], [0, 1, 0], [0, 0, -1], [0, 0, 1]]
        self.assertEqual(get_coordinates(test_tup), expected_output)

    def test_boundary_condition(self):
        test_tup = [10, 10, 10]
        expected_output = [[10, 10, 10], [9, 10, 10], [11, 10, 10], [10, 9, 10], [10, 11, 10], [10, 10, 9], [10, 10, 11]]
        self.assertEqual(get_coordinates(test_tup), expected_output)

    def test_invalid_input(self):
        test_tup = [1, '2', 3]
        with self.assertRaises(TypeError):
            get_coordinates(test_tup)
