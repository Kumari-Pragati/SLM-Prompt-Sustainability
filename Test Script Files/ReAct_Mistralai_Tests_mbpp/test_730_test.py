import unittest
from mbpp_730_code import consecutive_duplicates

class TestConsecutiveDuplicates(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(consecutive_duplicates([]), [])

    def test_single_element(self):
        self.assertEqual(consecutive_duplicates([1]), [1])

    def test_consecutive_duplicates(self):
        self.assertEqual(consecutive_duplicates([1, 1, 2, 1, 2, 3, 2, 2]), [1, 2, 3, 2])

    def test_duplicate_at_beginning(self):
        self.assertEqual(consecutive_duplicates([1, 1, 2]), [1, 2])

    def test_duplicate_at_end(self):
        self.assertEqual(consecutive_duplicates([1, 2, 1]), [1, 2])

    def test_duplicate_in_middle(self):
        self.assertEqual(consecutive_duplicates([1, 2, 1, 2, 1]), [1, 2])

    def test_consecutive_duplicates_with_gaps(self):
        self.assertEqual(consecutive_duplicates([1, 2, 3, 1, 2, 3]), [1, 2, 3])

    def test_consecutive_duplicates_with_non_consecutive_duplicates(self):
        self.assertEqual(consecutive_duplicates([1, 2, 1, 2, 3, 1, 2]), [1, 2, 3])

    def test_consecutive_duplicates_with_negative_numbers(self):
        self.assertEqual(consecutive_duplicates([-1, -1, 0, -1]), [-1, 0])

    def test_consecutive_duplicates_with_floats(self):
        self.assertEqual(consecutive_duplicates([1.1, 1.1, 2.2]), [1.1, 2.2])

    def test_consecutive_duplicates_with_non_numeric_values(self):
        self.assertEqual(consecutive_duplicates(["a", "a", "b"]), ["a"])
