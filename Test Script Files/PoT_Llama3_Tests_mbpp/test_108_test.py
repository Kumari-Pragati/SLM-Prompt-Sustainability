import unittest
from mbpp_108_code import merge_sorted_list

class TestMergeSortedList(unittest.TestCase):
    def test_typical_case(self):
        num1 = [1, 3, 5]
        num2 = [2, 4, 6]
        num3 = [0, 7, 8]
        self.assertEqual(merge_sorted_list(num1, num2, num3), [0, 1, 2, 3, 4, 5, 6, 7, 8])

    def test_edge_case_empty_list(self):
        num1 = []
        num2 = [1, 2, 3]
        num3 = []
        self.assertEqual(merge_sorted_list(num1, num2, num3), [1, 2, 3])

    def test_edge_case_single_list(self):
        num1 = [1, 2, 3]
        num2 = []
        num3 = []
        self.assertEqual(merge_sorted_list(num1, num2, num3), [1, 2, 3])

    def test_edge_case_all_empty_lists(self):
        num1 = []
        num2 = []
        num3 = []
        self.assertEqual(merge_sorted_list(num1, num2, num3), [])

    def test_edge_case_one_empty_list(self):
        num1 = [1, 2, 3]
        num2 = []
        num3 = [4, 5, 6]
        self.assertEqual(merge_sorted_list(num1, num2, num3), [1, 2, 3, 4, 5, 6])

    def test_edge_case_two_empty_lists(self):
        num1 = [1, 2, 3]
        num2 = []
        num3 = []
        self.assertEqual(merge_sorted_list(num1, num2, num3), [1, 2, 3])

    def test_edge_case_all_same_list(self):
        num1 = [1, 2, 3]
        num2 = [1, 2, 3]
        num3 = [1, 2, 3]
        self.assertEqual(merge_sorted_list(num1, num2, num3), [1, 2, 3])
