import unittest
from mbpp_414_code import overlapping

class TestOverlapping(unittest.TestCase):

    def test_empty_lists(self):
        self.assertEqual(overlapping([], []), 0)

    def test_single_element_lists(self):
        self.assertEqual(overlapping([1], [2]), 0)
        self.assertEqual(overlapping([1], [1]), 1)

    def test_multiple_element_lists(self):
        self.assertEqual(overlapping([1, 2, 3], [4, 5, 6]), 0)
        self.assertEqual(overlapping([1, 2, 3], [3, 4, 5]), 1)
        self.assertEqual(overlapping([1, 2, 3], [2, 3, 4]), 1)

    def test_duplicate_elements(self):
        self.assertEqual(overlapping([1, 2, 2], [2, 3, 4]), 1)
        self.assertEqual(overlapping([1, 2, 3], [2, 2, 4]), 1)
