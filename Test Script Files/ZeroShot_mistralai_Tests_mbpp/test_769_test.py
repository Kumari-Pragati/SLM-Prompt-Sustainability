import unittest
from mbpp_769_code import Diff

class TestDiff(unittest.TestCase):

    def test_empty_lists(self):
        self.assertEqual(Diff([]), [])
        self.assertEqual(Diff([], [1, 2, 3]), [1, 2, 3])
        self.assertEqual(Diff([1, 2, 3], []), [1, 2, 3])

    def test_single_element_lists(self):
        self.assertEqual(Diff([1], [1]), [])
        self.assertEqual(Diff([1], [2]), [1, 2])
        self.assertEqual(Diff([2], [1]), [2, 1])

    def test_equal_lists(self):
        self.assertEqual(Diff([1, 2, 3], [1, 2, 3]), [])

    def test_different_length_lists(self):
        self.assertEqual(Diff([1, 2, 3], [1, 2]), [3, ])
        self.assertEqual(Diff([1, 2], [1, 2, 3]), [3])

    def test_containment(self):
        self.assertEqual(Diff([1, 2, 3], [1, 2, 4]), [3])
        self.assertEqual(Diff([1, 2, 4], [1, 2, 3]), [4])

    def test_multiple_elements(self):
        self.assertEqual(Diff([1, 2, 3], [4, 5, 6]), [1, 2, 3, 4, 5, 6])
        self.assertEqual(Diff([4, 5, 6], [1, 2, 3]), [1, 2, 3, 4, 5, 6])
