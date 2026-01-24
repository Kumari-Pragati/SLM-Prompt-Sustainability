import unittest
from mbpp_414_code import overlapping

class TestOverlapping(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(overlapping([1, 2, 3], [3, 4, 5]), 1)
        self.assertEqual(overlapping([1, 1, 2], [1, 2, 3]), 1)
        self.assertEqual(overlapping([1, 2, 3], [1, 2, 3, 4]), 0)

    def test_edge_case_empty_lists(self):
        self.assertEqual(overlapping([], []), 0)
        self.assertEqual(overlapping([1], []), 0)
        self.assertEqual(overlapping([], [1]), 0)

    def test_edge_case_single_element(self):
        self.assertEqual(overlapping([1], [1]), 1)
        self.assertEqual(overlapping([1], [2]), 0)

    def test_corner_case_duplicate_elements(self):
        self.assertEqual(overlapping([1, 1, 2], [1, 2, 1]), 1)
        self.assertEqual(overlapping([1, 1, 1], [1, 1]), 1)
