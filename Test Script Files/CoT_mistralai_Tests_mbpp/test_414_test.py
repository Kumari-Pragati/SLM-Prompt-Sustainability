import unittest
from414_code import overlapping

class TestOverlapping(unittest.TestCase):
    def test_empty_lists(self):
        self.assertEqual(overlapping([]), 0)
        self.assertEqual(overlapping([], []), 0)

    def test_single_elements(self):
        self.assertEqual(overlapping([1], []), 0)
        self.assertEqual(overlapping([], [1]), 0)
        self.assertEqual(overlapping([1], [1]), 1)

    def test_identical_lists(self):
        self.assertEqual(overlapping([1, 2, 3], [3, 2, 1]), 1)
        self.assertEqual(overlapping([3, 2, 1], [1, 2, 3]), 1)

    def test_lists_with_duplicates(self):
        self.assertEqual(overlapping([1, 1, 2, 3], [3, 2, 1, 1]), 1)
        self.assertEqual(overlapping([3, 2, 1, 1], [1, 2, 3, 1]), 1)

    def test_lists_with_no_overlaps(self):
        self.assertEqual(overlapping([1, 2, 3], [4, 5, 6]), 0)
        self.assertEqual(overlapping([4, 5, 6], [1, 2, 3]), 0)

    def test_lists_with_different_lengths(self):
        self.assertEqual(overlapping([1, 2, 3], [1, 2]), 0)
        self.assertEqual(overlapping([1, 2], [1, 2, 3]), 0)

    def test_lists_with_negative_numbers(self):
        self.assertEqual(overlapping([1, -2, 3], [3, -2, 1]), 1)

    def test_lists_with_floats(self):
        self.assertEqual(overlapping([1.0, 2.0, 3.0], [3.0, 2.0, 1.0]), 1)

    def test_lists_with_strings(self):
        self.assertEqual(overlapping(["a", "b", "c"], ["c", "b", "a"]), 1)
