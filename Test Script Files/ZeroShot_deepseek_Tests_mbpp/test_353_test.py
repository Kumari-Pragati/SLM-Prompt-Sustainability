import unittest
from mbpp_353_code import remove_column

class TestRemoveColumn(unittest.TestCase):

    def test_remove_column(self):
        # Test with a list of lists
        list1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        n = 1
        expected_output = [[1, 3], [4, 6], [7, 9]]
        self.assertEqual(remove_column(list1, n), expected_output)

        # Test with a list of lists with different lengths
        list1 = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
        n = 3
        expected_output = [[1, 2], [5, 6], [9, 10]]
        self.assertEqual(remove_column(list1, n), expected_output)

        # Test with an empty list
        list1 = []
        n = 0
        expected_output = []
        self.assertEqual(remove_column(list1, n), expected_output)

        # Test with a list of lists with negative indices
        list1 = [[-1, -2, -3], [-4, -5, -6], [-7, -8, -9]]
        n = -1
        expected_output = [[-1, -3], [-4, -6], [-7, -9]]
        self.assertEqual(remove_column(list1, n), expected_output)

        # Test with a list of lists with out of range index
        list1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        n = 3
        expected_output = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        self.assertEqual(remove_column(list1, n), expected_output)
