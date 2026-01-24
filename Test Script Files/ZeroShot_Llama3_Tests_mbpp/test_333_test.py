import unittest
from mbpp_333_code import Sort

class TestSortFunction(unittest.TestCase):

    def test_sort_function(self):
        sub_li = [[5, 2], [1, 3], [2, 1], [4, 4]]
        expected_output = [[1, 3], [2, 1], [2, 2], [4, 4]]
        self.assertEqual(Sort(sub_li), expected_output)

        sub_li = [[5, 2], [1, 3], [2, 1], [4, 4], [3, 5]]
        expected_output = [[1, 3], [2, 1], [2, 2], [3, 5], [4, 4]]
        self.assertEqual(Sort(sub_li), expected_output)

        sub_li = [[5, 2], [1, 3], [2, 1], [4, 4], [3, 5], [6, 7]]
        expected_output = [[1, 3], [2, 1], [2, 2], [3, 5], [4, 4], [6, 7]]
        self.assertEqual(Sort(sub_li), expected_output)

    def test_sort_function_empty_list(self):
        sub_li = []
        expected_output = []
        self.assertEqual(Sort(sub_li), expected_output)

    def test_sort_function_single_element_list(self):
        sub_li = [[5, 2]]
        expected_output = [[5, 2]]
        self.assertEqual(Sort(sub_li), expected_output)
