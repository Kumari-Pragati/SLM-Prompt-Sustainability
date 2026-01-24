import unittest
from mbpp_946_code import most_common_elem

class TestMostCommonElem(unittest.TestCase):

    def test_typical_case(self):
        self.assertListEqual(most_common_elem("abccba", 2), [('c', 3)])
        self.assertListEqual(most_common_elem("hello", 2), [('l', 2), ('o', 2)])
        self.assertListEqual(most_common_elem("Python", 1), [('y', 1)])

    def test_edge_case_empty_list(self):
        self.assertListEqual(most_common_elem("", 1), [])

    def test_edge_case_single_element(self):
        self.assertListEqual(most_common_elem("a", 1), [('a', 1)])

    def test_edge_case_single_element_list(self):
        self.assertListEqual(most_common_elem(["a"], 1), [('a', 1)])

    def test_edge_case_multiple_elements_single_count(self):
        self.assertListEqual(most_common_elem("aa", 1), [('a', 2)])

    def test_edge_case_multiple_elements_multiple_count(self):
        self.assertListEqual(most_common_elem("aa", 2), [('a', 2)])

    def test_corner_case_duplicate_elements(self):
        self.assertListEqual(most_common_elem("aaabbb", 2), [('a', 3), ('b', 3)])
