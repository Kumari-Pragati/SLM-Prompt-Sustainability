import unittest
from mbpp_323_code import re_arrange

class TestReArrange(unittest.TestCase):

    def test_typical_case(self):
        arr = [1, -2, 3, -4, 5]
        n = len(arr)
        expected_output = [1, -2, 3, -4, 5]
        self.assertEqual(re_arrange(arr, n), expected_output)

    def test_edge_case(self):
        arr = [1]
        n = len(arr)
        expected_output = [1]
        self.assertEqual(re_arrange(arr, n), expected_output)

    def test_boundary_case(self):
        arr = [1, -1]
        n = len(arr)
        expected_output = [1, -1]
        self.assertEqual(re_arrange(arr, n), expected_output)

    def test_special_case(self):
        arr = [1, -1, 2, -2, 3, -3]
        n = len(arr)
        expected_output = [1, -1, 2, -2, 3, -3]
        self.assertEqual(re_arrange(arr, n), expected_output)

    def test_invalid_input(self):
        arr = [1, 2, 3]
        n = -1
        with self.assertRaises(ValueError):
            re_arrange(arr, n)
