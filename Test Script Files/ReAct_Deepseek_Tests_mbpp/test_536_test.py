import unittest
from mbpp_536_code import nth_items

class TestNthItems(unittest.TestCase):

    def test_typical_case(self):
        input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        n = 2
        expected_output = [1, 3, 5, 7, 9]
        self.assertEqual(nth_items(input_list, n), expected_output)

    def test_edge_case_n_equals_1(self):
        input_list = [1, 2, 3, 4, 5]
        n = 1
        expected_output = [1, 2, 3, 4, 5]
        self.assertEqual(nth_items(input_list, n), expected_output)

    def test_edge_case_n_equals_0(self):
        input_list = [1, 2, 3, 4, 5]
        n = 0
        with self.assertRaises(IndexError):
            nth_items(input_list, n)

    def test_edge_case_empty_list(self):
        input_list = []
        n = 2
        expected_output = []
        self.assertEqual(nth_items(input_list, n), expected_output)

    def test_typical_case_with_negative_n(self):
        input_list = [1, 2, 3, 4, 5]
        n = -2
        expected_output = [1, 3, 5]
        self.assertEqual(nth_items(input_list, n), expected_output)
