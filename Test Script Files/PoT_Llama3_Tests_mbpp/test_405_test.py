import unittest
from mbpp_405_code import check_tuplex

class TestCheckTuplex(unittest.TestCase):
    def test_typical_case(self):
        self.assertTrue(check_tuplex([1, 2, 3], (1, 2)))
    def test_edge_case_empty_tuple(self):
        self.assertFalse(check_tuplex([], (1, 2)))
    def test_edge_case_empty_list(self):
        self.assertFalse(check_tuplex([], ()))
    def test_edge_case_single_element_list(self):
        self.assertTrue(check_tuplex([1], (1,)))
    def test_edge_case_single_element_tuple(self):
        self.assertTrue(check_tuplex([1], (1,)))
    def test_edge_case_list_with_tuple(self):
        self.assertTrue(check_tuplex([1, 2, 3], (1, 2, 3)))
    def test_edge_case_tuple_with_list(self):
        self.assertTrue(check_tuplex((1, 2, 3), [1, 2, 3]))
    def test_edge_case_list_with_tuple_and_non_match(self):
        self.assertFalse(check_tuplex([1, 2, 3], (1, 2, 4)))
    def test_edge_case_tuple_with_list_and_non_match(self):
        self.assertFalse(check_tuplex((1, 2, 3), [1, 2, 4]))
