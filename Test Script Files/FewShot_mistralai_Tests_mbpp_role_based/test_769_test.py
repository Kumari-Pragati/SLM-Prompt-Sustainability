import unittest
from mbpp_769_code import Diff

class TestDiff(unittest.TestCase):
    def test_same_lists(self):
        self.assertEqual(Diff([1, 2, 3], [1, 2, 3]), [])

    def test_empty_lists(self):
        self.assertEqual(Diff([], []), [])

    def test_single_element_lists(self):
        self.assertEqual(Diff([1], []), [1])
        self.assertEqual(Diff([], [1]), [1])

    def test_equal_length_lists(self):
        self.assertEqual(Diff([1, 2, 3], [4, 2, 3]), [1])
        self.assertEqual(Diff([4, 2, 3], [1, 2, 3]), [4])

    def test_different_length_lists(self):
        self.assertEqual(Diff([1, 2, 3], [4, 2, 3, 5]), [1, 5])
        self.assertEqual(Diff([1, 2, 3, 5], [4, 2, 3]), [1, 5])

    def test_negative_numbers(self):
        self.assertEqual(Diff([-1, 2, -3], [-4, -2, 3]), [-1, -4])

    def test_duplicates(self):
        self.assertEqual(Diff([1, 1, 2, 3], [1, 2, 3]), [3])
        self.assertEqual(Diff([1, 2, 3], [1, 1, 2, 3]), [])
