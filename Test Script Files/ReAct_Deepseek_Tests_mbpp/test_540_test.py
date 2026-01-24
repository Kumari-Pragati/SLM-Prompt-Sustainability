import unittest
from mbpp_540_code import find_Diff

class TestFindDiff(unittest.TestCase):

    def test_typical_case(self):
        arr = [1, 2, 2, 3, 4, 4, 4, 5, 6]
        n = len(arr)
        self.assertEqual(find_Diff(arr, n), 2)

    def test_single_element(self):
        arr = [1]
        n = len(arr)
        self.assertEqual(find_Diff(arr, n), 0)

    def test_repeated_elements(self):
        arr = [1, 1, 1, 1, 1]
        n = len(arr)
        self.assertEqual(find_Diff(arr, n), 0)

    def test_sorted_array(self):
        arr = [1, 2, 3, 4, 5]
        n = len(arr)
        self.assertEqual(find_Diff(arr, n), 0)

    def test_reverse_sorted_array(self):
        arr = [5, 4, 3, 2, 1]
        n = len(arr)
        self.assertEqual(find_Diff(arr, n), 4)

    def test_empty_array(self):
        arr = []
        n = len(arr)
        self.assertEqual(find_Diff(arr, n), 0)

    def test_negative_numbers(self):
        arr = [-2, -1, 0, 1, 2]
        n = len(arr)
        self.assertEqual(find_Diff(arr, n), 2)

    def test_large_numbers(self):
        arr = [1000, 2000, 2000, 3000, 4000]
        n = len(arr)
        self.assertEqual(find_Diff(arr, n), 1000)
