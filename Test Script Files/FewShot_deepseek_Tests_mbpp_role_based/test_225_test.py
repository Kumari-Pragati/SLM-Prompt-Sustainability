import unittest
from mbpp_225_code import find_Min

class TestFindMin(unittest.TestCase):
    def test_typical_use_case(self):
        arr = [4, 5, 6, 7, 8, 9, 10, 1, 2, 3]
        self.assertEqual(find_Min(arr, 0, len(arr) - 1), 1)

    def test_edge_condition(self):
        arr = [1]
        self.assertEqual(find_Min(arr, 0, len(arr) - 1), 1)

    def test_boundary_condition(self):
        arr = [2, 1]
        self.assertEqual(find_Min(arr, 0, len(arr) - 1), 1)

    def test_invalid_input(self):
        arr = [1, 2, 3]
        with self.assertRaises(ValueError):
            find_Min(arr, 1, 2)
