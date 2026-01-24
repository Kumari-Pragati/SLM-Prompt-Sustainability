import unittest
from mbpp_414_code import overlapping

class TestOverlapping(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(overlapping([1, 2, 3], [3, 4, 5]), 1)
        self.assertEqual(overlapping([1, 2, 3], [4, 5, 6]), 0)

    def test_empty_lists(self):
        self.assertEqual(overlapping([], []), 0)

    def test_single_element_lists(self):
        self.assertEqual(overlapping([1], [1]), 1)
        self.assertEqual(overlapping([1], [2]), 0)

    def test_duplicate_elements(self):
        self.assertEqual(overlapping([1, 2, 2], [2, 3, 4]), 1)
        self.assertEqual(overlapping([1, 2, 3], [4, 5, 6]), 0)

    def test_large_lists(self):
        self.assertEqual(overlapping(list(range(1, 1001)), list(range(1001, 2001))), 0)
        self.assertEqual(overlapping(list(range(1, 1001)), list(range(1000, 2001))), 1)
