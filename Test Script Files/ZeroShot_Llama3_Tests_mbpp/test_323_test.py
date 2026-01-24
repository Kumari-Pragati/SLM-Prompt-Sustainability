import unittest
from mbpp_323_code import re_arrange

class TestReArrange(unittest.TestCase):

    def test_re_arrange(self):
        # Test case 1
        arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        n = len(arr)
        expected_output = [1, 3, 2, 5, 4, 7, 6, 9, 8, 10]
        self.assertEqual(re_arrange(arr, n), expected_output)

        # Test case 2
        arr = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10]
        n = len(arr)
        expected_output = [-1, -3, -2, -5, -4, -7, -6, -9, -8, -10]
        self.assertEqual(re_arrange(arr, n), expected_output)

        # Test case 3
        arr = [1, -2, 3, -4, 5, -6, 7, -8, 9, -10]
        n = len(arr)
        expected_output = [1, -2, 3, -4, 5, -6, 7, -8, 9, -10]
        self.assertEqual(re_arrange(arr, n), expected_output)

        # Test case 4
        arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
        n = len(arr)
        expected_output = [1, 3, 2, 5, 4, 7, 6, 9, 8, 11, 10]
        self.assertEqual(re_arrange(arr, n), expected_output)

        # Test case 5
        arr = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11]
        n = len(arr)
        expected_output = [-1, -3, -2, -5, -4, -7, -6, -9, -8, -11, -10]
        self.assertEqual(re_arrange(arr, n), expected_output)
