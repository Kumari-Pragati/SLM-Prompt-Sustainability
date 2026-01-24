import unittest
from mbpp_890_code import find_Extra

class TestFindExtra(unittest.TestCase):
    def test_typical_case(self):
        arr1 = [2, 4, 6, 8, 10]
        arr2 = [2, 4, 6, 8]
        n = len(arr1)
        self.assertEqual(find_Extra(arr1, arr2, n), n)

    def test_edge_case(self):
        arr1 = []
        arr2 = []
        n = 0
        self.assertEqual(find_Extra(arr1, arr2, n), n)

    def test_boundary_case(self):
        arr1 = [1]
        arr2 = []
        n = 1
        self.assertEqual(find_Extra(arr1, arr2, n), 0)

    def test_invalid_input(self):
        arr1 = [1, 2, 3]
        arr2 = [1, 2, 3, 4]
        n = 3
        with self.assertRaises(Exception):
            find_Extra(arr1, arr2, n)
