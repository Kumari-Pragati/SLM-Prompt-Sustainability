import unittest
from mbpp_627_code import find_First_Missing

class TestFindFirstMissing(unittest.TestCase):
    def test_empty_array(self):
        self.assertEqual(find_FirstMissing([], 0, len([])), 1)

    def test_single_element_array(self):
        self.assertEqual(find_FirstMissing([1], 0, 1), None)

    def test_consecutive_array(self):
        self.assertEqual(find_FirstMissing([1, 2, 3, 4], 0, 4), None)

    def test_missing_first_element(self):
        self.assertEqual(find_FirstMissing([2, 3, 4], 0, 3), 1)

    def test_missing_middle_element(self):
        self.assertEqual(find_FirstMissing([1, 2, 4], 0, 3), 3)

    def test_missing_last_element(self):
        self.assertEqual(find_FirstMissing([1, 2, 3], 0, 3), 4)

    def test_array_with_duplicates(self):
        self.assertEqual(find_FirstMissing([1, 1, 2, 3], 0, 3), None)

    def test_array_with_gaps(self):
        self.assertEqual(find_FirstMissing([1, 3, 4], 0, 2), 2)

    def test_array_with_negative_numbers(self):
        self.assertEqual(find_FirstMissing([-1, 0, 1, 2], 0, 3), -1)

    def test_array_with_zero(self):
        self.assertEqual(find_FirstMissing([0], 0, 0), 1)

    def test_array_with_large_numbers(self):
        self.assertEqual(find_FirstMissing([1000000001, 1, 2, 3, 4, 1000000002], 0, 5), 1000000001)

    def test_invalid_start_index(self):
        with self.assertRaises(IndexError):
            find_First_Missing([1, 2, 3], -1, 2)

    def test_invalid_end_index(self):
        with self.assertRaises(IndexError):
            find_First_Missing([1, 2, 3], 4, len([1, 2, 3]))
