import unittest
from mbpp_943_code import combine_lists

class TestCombineLists(unittest.TestCase):
    def test_typical_case(self):
        num1 = [1, 2, 3]
        num2 = [4, 5, 6]
        self.assertEqual(combine_lists(num1, num2), [1, 2, 3, 4, 5, 6])

    def test_edge_case_empty_list(self):
        num1 = []
        num2 = [4, 5, 6]
        self.assertEqual(combine_lists(num1, num2), [4, 5, 6])

    def test_edge_case_single_list(self):
        num1 = [1, 2, 3]
        num2 = []
        self.assertEqual(combine_lists(num1, num2), [1, 2, 3])

    def test_edge_case_sorted_lists(self):
        num1 = [1, 2, 3]
        num2 = [2, 3, 4]
        self.assertEqual(combine_lists(num1, num2), [1, 2, 2, 3, 3, 4])

    def test_edge_case_duplicates(self):
        num1 = [1, 2, 2]
        num2 = [2, 3, 3]
        self.assertEqual(combine_lists(num1, num2), [1, 2, 2, 2, 3, 3])

    def test_edge_case_empty_lists(self):
        num1 = []
        num2 = []
        self.assertEqual(combine_lists(num1, num2), [])
