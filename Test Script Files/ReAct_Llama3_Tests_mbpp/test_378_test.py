import unittest
from mbpp_378_code import move_first

class TestMoveFirst(unittest.TestCase):
    def test_typical_case(self):
        test_list = [1, 2, 3, 4, 5]
        expected_result = [5, 1, 2, 3, 4]
        self.assertEqual(move_first(test_list), expected_result)

    def test_edge_case_empty_list(self):
        test_list = []
        expected_result = []
        self.assertEqual(move_first(test_list), expected_result)

    def test_edge_case_single_element_list(self):
        test_list = [1]
        expected_result = [1]
        self.assertEqual(move_first(test_list), expected_result)

    def test_edge_case_list_with_duplicates(self):
        test_list = [1, 2, 2, 3, 1]
        expected_result = [1, 2, 2, 3, 1]
        self.assertEqual(move_first(test_list), expected_result)

    def test_edge_case_list_with_negative_numbers(self):
        test_list = [-1, -2, -3, -4, -5]
        expected_result = [-5, -1, -2, -3, -4]
        self.assertEqual(move_first(test_list), expected_result)
