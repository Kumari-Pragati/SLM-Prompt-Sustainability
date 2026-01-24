import unittest
from mbpp_414_code import overlapping

class TestOverlapping(unittest.TestCase):

    def test_empty_lists(self):
        self.assertEqual(overlapping([]), 0)
        self.assertEqual(overlapping([], []), 0)

    def test_single_elements(self):
        self.assertEqual(overlapping([1], [1]), 1)
        self.assertEqual(overlapping([1], []), 0)
        self.assertEqual(overlapping([], [1]), 0)

    def test_no_overlap(self):
        self.assertEqual(overlapping([1, 2, 3], [4, 5, 6]), 0)

    def test_overlap_one_element(self):
        self.assertEqual(overlapping([1, 2], [1, 2, 3]), 1)
        self.assertEqual(overlapping([1, 2], [1, 3]), 1)

    def test_overlap_multiple_elements(self):
        self.assertEqual(overlapping([1, 2, 3], [3, 4, 5]), 1)
        self.assertEqual(overlapping([1, 2, 3], [3, 2, 4]), 2)
