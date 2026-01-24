import unittest
from mbpp_414_code import overlapping

class TestOverlapping(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(overlapping([1, 2, 3], [2, 3, 4]), 1)

    def test_empty_lists(self):
        self.assertEqual(overlapping([], []), 0)

    def test_one_element_in_both_lists(self):
        self.assertEqual(overlapping([1], [1]), 1)

    def test_no_overlap(self):
        self.assertEqual(overlapping([1, 2, 3], [4, 5, 6]), 0)

    def test_duplicate_elements(self):
        self.assertEqual(overlapping([1, 2, 2], [2, 3, 4]), 1)

    def test_same_elements_in_different_order(self):
        self.assertEqual(overlapping([2, 3, 1], [1, 2, 3]), 1)

    def test_large_lists(self):
        self.assertEqual(overlapping(list(range(1, 1001)), list(range(1000, 2001))), 1)

    def test_negative_numbers(self):
        self.assertEqual(overlapping([-1, -2, -3], [-3, -4, -5]), 1)

    def test_mixed_types(self):
        self.assertEqual(overlapping([1, '2', 3], [1, 2, 3]), 1)
