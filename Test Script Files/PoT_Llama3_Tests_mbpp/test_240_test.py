import unittest
from mbpp_240_code import replace_list

class TestReplaceList(unittest.TestCase):

    def test_typical_case(self):
        list1 = [1, 2, 3]
        list2 = [4, 5, 6]
        result = replace_list(list1, list2)
        self.assertEqual(result, [1, 2, 3, 4, 5, 6])

    def test_edge_case_empty_list1(self):
        list1 = []
        list2 = [4, 5, 6]
        result = replace_list(list1, list2)
        self.assertEqual(result, [])

    def test_edge_case_empty_list2(self):
        list1 = [1, 2, 3]
        list2 = []
        result = replace_list(list1, list2)
        self.assertEqual(result, [1, 2, 3])

    def test_edge_case_list1_empty(self):
        list1 = []
        list2 = [4, 5, 6]
        result = replace_list(list1, list2)
        self.assertEqual(result, [])

    def test_edge_case_list2_empty(self):
        list1 = [1, 2, 3]
        list2 = []
        result = replace_list(list1, list2)
        self.assertEqual(result, [1, 2, 3])

    def test_edge_case_list1_single_element(self):
        list1 = [1]
        list2 = [4, 5, 6]
        result = replace_list(list1, list2)
        self.assertEqual(result, [1, 4, 5, 6])

    def test_edge_case_list2_single_element(self):
        list1 = [1, 2, 3]
        list2 = [4]
        result = replace_list(list1, list2)
        self.assertEqual(result, [1, 2, 3, 4])

    def test_edge_case_list1_single_element_list2_empty(self):
        list1 = [1]
        list2 = []
        result = replace_list(list1, list2)
        self.assertEqual(result, [1])

    def test_edge_case_list2_single_element_list1_empty(self):
        list1 = []
        list2 = [4]
        result = replace_list(list1, list2)
        self.assertEqual(result, [])
