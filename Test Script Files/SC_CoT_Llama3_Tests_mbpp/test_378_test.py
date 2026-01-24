import unittest
from mbpp_378_code import move_first

class TestMoveFirst(unittest.TestCase):

    def test_typical_input(self):
        test_list = [1, 2, 3, 4, 5]
        result = move_first(test_list)
        self.assertEqual(result, [5, 1, 2, 3, 4])

    def test_edge_case_empty_list(self):
        test_list = []
        result = move_first(test_list)
        self.assertEqual(result, [])

    def test_edge_case_single_element_list(self):
        test_list = [1]
        result = move_first(test_list)
        self.assertEqual(result, [1])

    def test_edge_case_list_with_one_element(self):
        test_list = [1, 2]
        result = move_first(test_list)
        self.assertEqual(result, [2, 1])

    def test_edge_case_list_with_two_elements(self):
        test_list = [1, 2, 3]
        result = move_first(test_list)
        self.assertEqual(result, [3, 1, 2])

    def test_edge_case_list_with_three_elements(self):
        test_list = [1, 2, 3, 4]
        result = move_first(test_list)
        self.assertEqual(result, [4, 1, 2, 3])

    def test_edge_case_list_with_four_elements(self):
        test_list = [1, 2, 3, 4, 5]
        result = move_first(test_list)
        self.assertEqual(result, [5, 1, 2, 3, 4])

    def test_edge_case_list_with_five_elements(self):
        test_list = [1, 2, 3, 4, 5, 6]
        result = move_first(test_list)
        self.assertEqual(result, [6, 1, 2, 3, 4, 5])

    def test_invalid_input_non_list(self):
        test_list = "hello"
        with self.assertRaises(TypeError):
            move_first(test_list)
