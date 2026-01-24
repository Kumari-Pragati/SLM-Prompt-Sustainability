import unittest
from mbpp_414_code import overlapping

class TestOverlapping(unittest.TestCase):
    def test_empty_lists(self):
        self.assertEqual(overlapping([], []), 0)

    def test_single_element_lists(self):
        self.assertEqual(overlapping([1], [1]), 1)
        self.assertEqual(overlapping([1], [2]), 0)
        self.assertEqual(overlapping([1, 2], [1]), 1)
        self.assertEqual(overlapping([1, 2], [3]), 0)

    def test_multiple_element_lists(self):
        self.assertEqual(overlapping([1, 2, 3], [1, 2, 3]), 1)
        self.assertEqual(overlapping([1, 2, 3], [1, 2, 4]), 1)
        self.assertEqual(overlapping([1, 2, 3], [1, 2, 5]), 0)
        self.assertEqual(overlapping([1, 2, 3], [4, 5, 6]), 0)

    def test_duplicates_in_lists(self):
        self.assertEqual(overlapping([1, 1, 2], [1, 2, 2]), 1)
        self.assertEqual(overlapping([1, 1, 2], [1, 2, 3]), 1)
        self.assertEqual(overlapping([1, 1, 2], [4, 5, 6]), 0)
