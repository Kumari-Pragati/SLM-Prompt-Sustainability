import unittest
from mbpp_642_code import remove_similar_row

class TestRemoveSimilarRow(unittest.TestCase):
    def test_typical_use_case(self):
        test_list = [[1, 2, 3], [2, 3, 1], [3, 1, 2], [4, 5, 6]]
        expected_output = {(1, 2, 3), (4, 5, 6)}
        self.assertEqual(remove_similar_row(test_list), expected_output)

    def test_empty_list(self):
        test_list = []
        expected_output = set()
        self.assertEqual(remove_similar_row(test_list), expected_output)

    def test_single_element(self):
        test_list = [[1]]
        expected_output = {(1,)}
        self.assertEqual(remove_similar_row(test_list), expected_output)

    def test_duplicate_elements(self):
        test_list = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
        expected_output = {(1,), (2,), (3,)}
        self.assertEqual(remove_similar_row(test_list), expected_output)

    def test_unsorted_elements(self):
        test_list = [[3, 1, 2], [2, 3, 1], [1, 2, 3]]
        expected_output = {(1, 2, 3)}
        self.assertEqual(remove_similar_row(test_list), expected_output)

    def test_negative_numbers(self):
        test_list = [[-1, -2, -3], [-2, -3, -1], [-3, -1, -2]]
        expected_output = {(-1, -2, -3)}
        self.assertEqual(remove_similar_row(test_list), expected_output)
