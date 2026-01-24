import unittest
from627_code import find_First_Missing

class TestFindFirstMissing(unittest.TestCase):

    def test_empty_array(self):
        self.assertEqual(find_FirstMissing([], 0, len([]) - 1), 1)

    def test_single_element_array(self):
        for i in range(1, 101):
            self.assertEqual(find_FirstMissing([i], 0, len([i]) - 1), None)

    def test_consecutive_array(self):
        for i in range(1, 101):
            arr = list(range(1, i + 2))
            self.assertEqual(find_FirstMissing(arr, 0, len(arr) - 1), None)

    def test_missing_first_element(self):
        arr = [2, 3, 4, 5, 6]
        self.assertEqual(find_FirstMissing(arr, 0, len(arr) - 1), 1)

    def test_missing_last_element(self):
        arr = [1, 2, 3, 4, 5]
        self.assertEqual(find_FirstMissing(arr, 0, len(arr) - 1), 6)

    def test_missing_middle_element(self):
        arr = [1, 2, 4, 5]
        self.assertEqual(find_FirstMissing(arr, 0, len(arr) - 1), 3)

    def test_negative_start(self):
        self.assertRaises(IndexError, find_FirstMissing, [1, 2, 3], -1, 2)

    def test_negative_end(self):
        self.assertRaises(IndexError, find_FirstMissing, [1, 2, 3], 0, -1)

    def test_start_greater_than_end(self):
        self.assertEqual(find_FirstMissing([1, 2, 3], 4, 0), 1)

    def test_array_with_duplicates(self):
        arr = [1, 1, 2, 3, 4, 4, 5]
        self.assertEqual(find_FirstMissing(arr, 0, len(arr) - 1), 2)
