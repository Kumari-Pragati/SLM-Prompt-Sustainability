import unittest
from mbpp_630_code import get_coordinates

class TestGetCoordinates(unittest.TestCase):

    def test_typical_case(self):
        test_tup = [(1, 2), (3, 4), (5, 6)]
        expected_output = [
            [1, 2, 3],
            [1, 2, 4],
            [1, 2, 5],
            [1, 3, 4],
            [1, 3, 5],
            [1, 4, 5],
            [2, 3, 4],
            [2, 3, 5],
            [2, 4, 5],
            [3, 4, 5]
        ]
        self.assertEqual(get_coordinates(test_tup), expected_output)

    def test_empty_tuple(self):
        test_tup = []
        expected_output = [[]]
        self.assertEqual(get_coordinates(test_tup), expected_output)

    def test_single_element_tuple(self):
        test_tup = [(1,)]
        expected_output = [[1]]
        self.assertEqual(get_coordinates(test_tup), expected_output)

    def test_negative_elements(self):
        test_tup = [(-1, 2), (3, 4), (5, 6)]
        expected_output = [
            [-1, 2, 3],
            [-1, 2, 4],
            [-1, 2, 5],
            [-1, 3, 4],
            [-1, 3, 5],
            [-1, 4, 5],
            [0, 3, 4],
            [0, 3, 5],
            [0, 4, 5],
            [1, 4, 5]
        ]
        self.assertEqual(get_coordinates(test_tup), expected_output)

    def test_large_elements(self):
        test_tup = [(100, 200), (300, 400), (500, 600)]
        # This test case is to ensure that the function can handle large numbers
        self.assertTrue(get_coordinates(test_tup))
