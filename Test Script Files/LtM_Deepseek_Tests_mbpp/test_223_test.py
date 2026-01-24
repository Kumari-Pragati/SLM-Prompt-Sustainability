import unittest
from mbpp_223_code import binary_search

class TestBinarySearch(unittest.TestCase):

    def test_simple_input(self):
        arr = [1, 2, 3, 4, 5]
        self.assertEqual(binary_search(arr, 0, len(arr)-1, 4), 3)

    def test_edge_conditions(self):
        # Test when element is not present
        arr = [1, 2, 3, 4, 5]
        self.assertEqual(binary_search(arr, 0, len(arr)-1, 6), -1)

        # Test with single element array
        arr = [5]
        self.assertEqual(binary_search(arr, 0, len(arr)-1, 5), 0)

        # Test with empty array
        arr = []
        self.assertEqual(binary_search(arr, 0, len(arr)-1, 5), -1)

    def test_complex_cases(self):
        # Test with duplicate elements
        arr = [1, 2, 2, 3, 4, 5]
        self.assertEqual(binary_search(arr, 0, len(arr)-1, 2), 1)

        # Test with elements at the ends of the array
        arr = [1, 2, 3, 4, 5]
        self.assertEqual(binary_search(arr, 0, len(arr)-1, 1), 0)
        self.assertEqual(binary_search(arr, 0, len(arr)-1, 5), 4)

        # Test with elements at the beginning and end of the array
        arr = [1, 2, 3, 4, 5]
        self.assertEqual(binary_search(arr, 0, len(arr)-1, 3), 2)
