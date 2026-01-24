import unittest
from mbpp_378_code import move_first

class TestMoveFirst(unittest.TestCase):
    def test_typical_use_case(self):
        test_list = [1, 2, 3, 4, 5]
        expected_result = [5, 1, 2, 3, 4]
        self.assertEqual(move_first(test_list), expected_result)

    def test_empty_list(self):
        test_list = []
        expected_result = []
        self.assertEqual(move_first(test_list), expected_result)

    def test_single_element_list(self):
        test_list = [1]
        expected_result = [1]
        self.assertEqual(move_first(test_list), expected_result)

    def test_list_with_duplicates(self):
        test_list = [1, 2, 2, 3, 4, 4]
        expected_result = [4, 4, 2, 2, 3, 1]
        self.assertEqual(move_first(test_list), expected_result)
