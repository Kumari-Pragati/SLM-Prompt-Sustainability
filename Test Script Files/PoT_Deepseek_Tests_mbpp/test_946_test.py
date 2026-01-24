import unittest
from mbpp_946_code import most_common_elem

class TestMostCommonElem(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(most_common_elem('aabbbcc', 2), [('b', 3), ('a', 2)])

    def test_edge_case_single_most_common(self):
        self.assertEqual(most_common_elem('aabbbcc', 1), [('b', 3)])

    def test_boundary_case_empty_string(self):
        self.assertEqual(most_common_elem('', 2), [])

    def test_boundary_case_a_equals_0(self):
        self.assertEqual(most_common_elem('aabbbcc', 0), [])

    def test_corner_case_all_same_elements(self):
        self.assertEqual(most_common_elem('aaaaa', 3), [('a', 5)])

    def test_corner_case_all_different_elements(self):
        self.assertEqual(most_common_elem('abcdefg', 3), [('g', 1), ('f', 1), ('e', 1)])

    def test_corner_case_a_greater_than_unique_elements(self):
        self.assertEqual(most_common_elem('aabbbcc', 7), [('b', 3), ('a', 2), ('c', 2)])
