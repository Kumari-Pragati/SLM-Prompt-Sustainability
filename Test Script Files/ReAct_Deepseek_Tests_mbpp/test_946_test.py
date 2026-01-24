import unittest
from mbpp_946_code import most_common_elem

class TestMostCommonElem(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(most_common_elem([1, 2, 2, 3, 3, 3, 4, 4, 4, 4], 2), [(4, 4), (3, 3)])

    def test_single_element(self):
        self.assertEqual(most_common_elem([1], 1), [(1, 1)])

    def test_empty_list(self):
        self.assertEqual(most_common_elem([], 1), [])

    def test_negative_elements(self):
        self.assertEqual(most_common_elem([-1, -1, 2, 2, 3, 3], 2), [(-1, 2), (2, 2)])

    def test_zero_elements(self):
        self.assertEqual(most_common_elem([0, 0, 1, 1], 2), [(0, 2), (1, 2)])

    def test_most_common_with_one(self):
        self.assertEqual(most_common_elem([1, 2, 2, 3, 3, 3, 4, 4, 4, 4], 1), [(4, 4)])

    def test_most_common_with_zero(self):
        self.assertEqual(most_common_elem([1, 2, 2, 3, 3, 3, 4, 4, 4, 4], 0), [])

    def test_most_common_with_more_than_elements(self):
        self.assertEqual(most_common_elem([1, 2, 2, 3, 3, 3, 4, 4, 4, 4], 11), [(4, 4), (3, 3), (2, 2), (1, 1)])

    def test_most_common_with_negative_count(self):
        self.assertEqual(most_common_elem([1, 2, 2, 3, 3, 3, 4, 4, 4, 4], -1), [])
