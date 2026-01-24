import unittest
from mbpp_947_code import len_log

class TestLenLog(unittest.TestCase):
    def test_typical(self):
        self.assertEqual(len_log([[1,2,3], [4,5,6], [7,8,9]]), 3)

    def test_edge_case_empty_list(self):
        self.assertEqual(len_log([]), None)

    def test_edge_case_single_element_list(self):
        self.assertEqual(len_log([[1,2,3]]), 3)

    def test_edge_case_single_element_list_empty(self):
        self.assertEqual(len_log([[]]), None)

    def test_edge_case_single_element_list_single_element(self):
        self.assertEqual(len_log([['a']]), 1)

    def test_edge_case_single_element_list_single_element_empty(self):
        self.assertEqual(len_log([['']]), None)

    def test_edge_case_multiple_single_element_lists(self):
        self.assertEqual(len_log([['a'], ['b'], ['c']]), 1)

    def test_edge_case_multiple_single_element_lists_empty(self):
        self.assertEqual(len_log([[''], ['',], ['',,'']]), None)

    def test_edge_case_multiple_single_element_lists_single_element(self):
        self.assertEqual(len_log([['a'], ['b'], ['c']]), 1)

    def test_edge_case_multiple_single_element_lists_single_element_empty(self):
        self.assertEqual(len_log([[''], ['',], ['',,'']]), None)

    def test_edge_case_multiple_single_element_lists_single_element_empty(self):
        self.assertEqual(len_log([[''], ['',], ['',,'']]), None)

    def test_edge_case_multiple_single_element_lists_single_element_single_element(self):
        self.assertEqual(len_log([['a'], ['b'], ['c']]), 1)

    def test_edge_case_multiple_single_element_lists_single_element_single_element_empty(self):
        self.assertEqual(len_log([[''], ['',], ['',,'']]), None)

    def test_edge_case_multiple_single_element_lists_single_element_single_element_empty(self):
        self.assertEqual(len_log([[''], ['',], ['',,'']]), None)

    def test_edge_case_multiple_single_element_lists_single_element_single_element_single_element(self):
        self.assertEqual(len_log([['a'], ['b'], ['c']]), 1)

    def test_edge_case_multiple_single_element_lists_single_element_single_element_single_element_empty(self):
        self.assertEqual(len_log([[''], ['',], ['',,'']]), None)
