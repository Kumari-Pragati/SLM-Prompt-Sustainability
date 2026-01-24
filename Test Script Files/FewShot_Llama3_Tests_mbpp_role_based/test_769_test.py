import unittest
from mbpp_769_code import Diff

class TestDiff(unittest.TestCase):
    def test_empty_lists(self):
        self.assertEqual(Diff([], []), [])

    def test_single_element_lists(self):
        self.assertEqual(Diff([1], [1]), [])
        self.assertEqual(Diff([1], []), [1])
        self.assertEqual(Diff([], [1]), [1])

    def test_common_elements(self):
        self.assertEqual(Diff([1, 2, 3], [2, 3, 4]), [1, 4])
        self.assertEqual(Diff([1, 2, 3], [1, 2, 3]), [])

    def test_non_common_elements(self):
        self.assertEqual(Diff([1, 2, 3], [4, 5, 6]), [1, 2, 3, 4, 5, 6])
        self.assertEqual(Diff([1, 2, 3], [7, 8, 9]), [1, 2, 3, 7, 8, 9])

    def test_duplicates(self):
        self.assertEqual(Diff([1, 1, 2, 2, 3], [1, 1, 2, 2, 3]), [])
        self.assertEqual(Diff([1, 1, 2, 2, 3], [1, 2, 3]), [1, 1, 2, 2, 3])
