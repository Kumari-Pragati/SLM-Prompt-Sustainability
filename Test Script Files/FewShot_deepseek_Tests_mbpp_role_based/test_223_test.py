import unittest
from mbpp_223_code import binary_search

class TestBinarySearch(unittest.TestCase):
    def test_typical_use_case(self):
        arr = [2, 3, 4, 10, 40]
        x = 10
        result = binary_search(arr, 0, len(arr)-1, x)
        self.assertEqual(result, 3)

    def test_edge_condition(self):
        arr = [2]
        x = 2
        result = binary_search(arr, 0, len(arr)-1, x)
        self.assertEqual(result, 0)

    def test_boundary_condition(self):
        arr = [2, 3, 4, 10, 40]
        x = 50
        result = binary_search(arr, 0, len(arr)-1, x)
        self.assertEqual(result, -1)

    def test_invalid_input(self):
        arr = [2, 3, 4, 10, 40]
        x = 'a'
        with self.assertRaises(TypeError):
            binary_search(arr, 0, len(arr)-1, x)
