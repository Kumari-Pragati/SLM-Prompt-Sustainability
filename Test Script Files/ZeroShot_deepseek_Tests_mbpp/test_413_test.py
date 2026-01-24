import unittest
from mbpp_413_code import extract_nth_element

class TestExtractNthElement(unittest.TestCase):

    def test_extract_nth_element(self):
        # Test with a list of lists with varying lengths
        list1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        n = 1
        self.assertEqual(extract_nth_element(list1, n), [2, 5, 8])

        # Test with a list of lists with duplicate values
        list1 = [[1, 2, 3], [4, 4, 6], [7, 8, 9]]
        n = 1
        self.assertEqual(extract_nth_element(list1, n), [2, 4, 8])

        # Test with a list of lists with negative numbers
        list1 = [[-1, -2, -3], [-4, -5, -6], [-7, -8, -9]]
        n = 1
        self.assertEqual(extract_nth_element(list1, n), [-2, -5, -8])

        # Test with a list of lists with zero
        list1 = [[0, 2, 3], [4, 5, 6], [7, 8, 9]]
        n = 1
        self.assertEqual(extract_nth_element(list1, n), [2, 5, 8])

        # Test with a list of lists with a large number
        list1 = [[1000000000, 2, 3], [4, 5, 6], [7, 8, 9]]
        n = 1
        self.assertEqual(extract_nth_element(list1, n), [2, 5, 8])

        # Test with a list of lists with a negative index
        list1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        n = -1
        self.assertEqual(extract_nth_element(list1, n), [3, 6, 9])

        # Test with an empty list
        list1 = []
        n = 1
        self.assertEqual(extract_nth_element(list1, n), [])

        # Test with a list of lists with a single element
        list1 = [[1]]
        n = 0
        self.assertEqual(extract_nth_element(list1, n), [1])

        # Test with a list of lists with a large index
        list1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        n = 10
        self.assertEqual(extract_nth_element(list1, n), [])

        # Test with a list of lists with a negative large index
        list1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        n = -10
        self.assertEqual(extract_nth_element(list1, n), [])
