import unittest
from mbpp_225_code import find_Min

class TestFindMin(unittest.TestCase):

    def test_empty_list(self):
        with self.assertRaises(IndexError):
            find_Min([], 0, 0)

    def test_single_element(self):
        self.assertEqual(find_Min([1], 0, 0), 1)

    def test_single_element_end(self):
        self.assertEqual(find_Min([1], 1, 1), 1)

    def test_duplicate_elements(self):
        self.assertEqual(find_Min([1, 1, 3, 5]), 1)

    def test_duplicate_elements_end(self):
        self.assertEqual(find_Min([1, 1, 3, 1]), 1)

    def test_increasing_sequence(self):
        self.assertEqual(find_Min([1, 2, 3, 4, 5]), 1)

    def test_decreasing_sequence(self):
        self.assertEqual(find_Min([5, 4, 3, 2, 1]), 1)

    def test_mixed_sequence(self):
        self.assertEqual(find_Min([1, 5, 2, 3, 4]), 1)

    def test_mixed_sequence_end(self):
        self.assertEqual(find_Min([1, 5, 2, 3, 1]), 1)

    def test_negative_numbers(self):
        self.assertEqual(find_Min([-1, -2, -3, -4, -5]), -1)

    def test_negative_numbers_end(self):
        self.assertEqual(find_Min([-1, -2, -3, -4, -1]), -1)

    def test_negative_and_positive_numbers(self):
        self.assertEqual(find_Min([1, -1, 3, -3, 5]), 1)

    def test_negative_and_positive_numbers_end(self):
        self.assertEqual(find_Min([1, -1, 3, -3, 1]), 1)

    def test_large_sequence(self):
        arr = [i for i in range(1000)]
        self.assertEqual(find_Min(arr), arr[0])
