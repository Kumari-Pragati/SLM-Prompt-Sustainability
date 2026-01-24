import unittest
from mbpp_642_code import remove_similar_row

class TestRemoveSimilarRow(unittest.TestCase):

    def test_typical_case(self):
        test_list = [[1, 2, 3], [2, 1, 3], [3, 2, 1], [1, 2, 2]]
        expected_output = {(1, 2, 3), (2, 1, 3), (3, 1, 2)}
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

    def test_mixed_elements(self):
        test_list = [[1, 2, 3], [3, 2, 1], [2, 3, 1], [1, 3, 2]]
        expected_output = {(1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)}
        self.assertEqual(remove_similar_row(test_list), expected_output)

    def test_invalid_input(self):
        test_list = [1, 2, 3]
        with self.assertRaises(TypeError):
            remove_similar_row(test_list)
