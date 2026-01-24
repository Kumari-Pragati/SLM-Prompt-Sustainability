import unittest
from mbpp_665_code import move_last

class TestMoveLast(unittest.TestCase):
    def test_typical_use_case(self):
        num_list = [1, 2, 2, 3, 4, 4, 4]
        expected_output = [2, 2, 3, 4, 4, 4, 1]
        self.assertEqual(move_last(num_list), expected_output)

    def test_edge_case_single_element(self):
        num_list = [1]
        expected_output = [1]
        self.assertEqual(move_last(num_list), expected_output)

    def test_edge_case_empty_list(self):
        num_list = []
        expected_output = []
        self.assertEqual(move_last(num_list), expected_output)

    def test_edge_case_all_duplicates(self):
        num_list = [1, 1, 1, 1]
        expected_output = [1, 1, 1, 1]
        self.assertEqual(move_last(num_list), expected_output)

    def test_edge_case_all_unique(self):
        num_list = [1, 2, 3, 4, 5]
        expected_output = [1, 2, 3, 4, 5]
        self.assertEqual(move_last(num_list), expected_output)
