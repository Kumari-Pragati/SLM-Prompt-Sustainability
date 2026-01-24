import unittest
from mbpp_353_code import remove_column

class TestRemoveColumn(unittest.TestCase):

    def test_simple_input(self):
        list1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        n = 1
        expected_output = [[1, 3], [4, 6], [7, 9]]
        self.assertEqual(remove_column(list1, n), expected_output)

    def test_edge_condition_empty_list(self):
        list1 = []
        n = 0
        expected_output = []
        self.assertEqual(remove_column(list1, n), expected_output)

    def test_edge_condition_single_element_list(self):
        list1 = [[1]]
        n = 0
        expected_output = []
        self.assertEqual(remove_column(list1, n), expected_output)

    def test_edge_condition_negative_index(self):
        list1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        n = -1
        expected_output = [[1, 2], [4, 5], [7, 8]]
        self.assertEqual(remove_column(list1, n), expected_output)

    def test_edge_condition_index_out_of_range(self):
        list1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        n = 3
        expected_output = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        self.assertEqual(remove_column(list1, n), expected_output)
