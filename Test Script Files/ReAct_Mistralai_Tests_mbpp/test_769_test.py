import unittest
from mbpp_769_code import Diff

class TestDiff(unittest.TestCase):

    def test_empty_lists(self):
        self.assertEqual(Diff([]), [])

    def test_single_element_lists(self):
        self.assertEqual(Diff([1], []), [1])
        self.assertEqual(Diff([], [1]), [1])

    def test_identical_lists(self):
        self.assertEqual(Diff([1, 2, 3], [1, 2, 3]), [])

    def test_different_lengths(self):
        self.assertEqual(Diff([1, 2, 3], [1, 2]), [3])
        self.assertEqual(Diff([1, 2], [1, 2, 3]), [3])

    def test_duplicates_in_lists(self):
        self.assertEqual(Diff([1, 1, 2, 3], [1, 2, 2, 3]), [1])
        self.assertEqual(Diff([1, 2, 3], [1, 1, 2, 3]), [])

    def test_negative_numbers(self):
        self.assertEqual(Diff([1, -1, 2], [1, -2, 3]), [-1, 2])
        self.assertEqual(Diff([-1, 1, 2], [-1, 1, 2]), [])

    def test_mixed_types(self):
        self.assertEqual(Diff([1, 'a', 2], [1, 'b', 3]), ['a', 'b'])
        self.assertEqual(Diff([1, 'a'], [1, 'b', 2]), ['a'])
