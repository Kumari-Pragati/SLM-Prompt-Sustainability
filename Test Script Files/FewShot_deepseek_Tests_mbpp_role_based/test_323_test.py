import unittest
from mbpp_323_code import re_arrange

class TestReArrange(unittest.TestCase):
    def test_typical_case(self):
        arr = [1, -2, 3, -4, 5]
        n = len(arr)
        expected_output = [1, -2, 3, -4, 5]
        self.assertEqual(re_arrange(arr, n), expected_output)

    def test_boundary_conditions(self):
        # Test with an empty array
        arr = []
        n = len(arr)
        expected_output = []
        self.assertEqual(re_arrange(arr, n), expected_output)

        # Test with an array of size 1
        arr = [1]
        n = len(arr)
        expected_output = [1]
        self.assertEqual(re_arrange(arr, n), expected_output)

    def test_error_handling(self):
        # Test with a non-integer array
        arr = [1, -2, 3, -4, 'a']
        n = len(arr)
        with self.assertRaises(TypeError):
            re_arrange(arr, n)

        # Test with a negative size
        arr = [1, -2, 3, -4, 5]
        n = -1
        with self.assertRaises(ValueError):
            re_arrange(arr, n)

    def test_edge_cases(self):
        # Test with all positive numbers
        arr = [1, 2, 3, 4, 5]
        n = len(arr)
        expected_output = [1, 2, 3, 4, 5]
        self.assertEqual(re_arrange(arr, n), expected_output)

        # Test with all negative numbers
        arr = [-1, -2, -3, -4, -5]
        n = len(arr)
        expected_output = [-1, -2, -3, -4, -5]
        self.assertEqual(re_arrange(arr, n), expected_output)

        # Test with mixed positive and negative numbers
        arr = [1, -1, 2, -2, 3, -3]
        n = len(arr)
        expected_output = [1, -1, 2, -2, 3, -3]
        self.assertEqual(re_arrange(arr, n), expected_output)
