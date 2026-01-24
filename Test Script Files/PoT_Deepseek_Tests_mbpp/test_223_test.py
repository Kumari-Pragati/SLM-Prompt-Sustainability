import unittest
from mbpp_223_code import binary_search

class TestBinarySearch(unittest.TestCase):

    def test_typical_cases(self):
        arr = [1, 2, 3, 4, 5]
        self.assertEqual(binary_search(arr, 0, len(arr)-1, 3), 2)
        self.assertEqual(binary_search(arr, 0, len(arr)-1, 5), 4)

    def test_edge_cases(self):
        arr = [1, 2, 3, 4, 5]
        self.assertEqual(binary_search(arr, 0, len(arr)-1, 1), 0)
        self.assertEqual(binary_search(arr, 0, len(arr)-1, 5), 4)

    def test_boundary_conditions(self):
        arr = [1, 2, 3, 4, 5]
        self.assertEqual(binary_search(arr, 0, len(arr)-1, 0), -1)
        self.assertEqual(binary_search(arr, 0, len(arr)-1, 6), -1)

    def test_invalid_inputs(self):
        arr = [1, 2, 3, 4, 5]
        with self.assertRaises(TypeError):
            binary_search(arr, 'a', len(arr)-1, 3)
        with self.assertRaises(TypeError):
            binary_search(arr, 0, 'b', 3)
        with self.assertRaises(TypeError):
            binary_search(arr, 0, 1, 'c')
