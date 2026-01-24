import unittest
from mbpp_908_code import find_fixed_point

class TestFindFixedPoint(unittest.TestCase):
    def test_found_fixed_point(self):
        arr = [0, 1, 2, 3, 4, 5]
        n = len(arr)
        self.assertEqual(find_fixed_point(arr, n), 0)

    def test_not_found_fixed_point(self):
        arr = [0, 1, 2, 3, 4, 5]
        n = len(arr)
        self.assertEqual(find_fixed_point(arr, n), -1)

    def test_empty_array(self):
        arr = []
        n = len(arr)
        self.assertEqual(find_fixed_point(arr, n), -1)

    def test_single_element_array(self):
        arr = [0]
        n = len(arr)
        self.assertEqual(find_fixed_point(arr, n), 0)

    def test_negative_numbers(self):
        arr = [-1, 0, 1, 2, 3, 4]
        n = len(arr)
        self.assertEqual(find_fixed_point(arr, n), 0)

    def test_non_integer_array(self):
        arr = [0.0, 1.0, 2.0, 3.0, 4.0, 5.0]
        n = len(arr)
        self.assertEqual(find_fixed_point(arr, n), -1)
