import unittest
from mbpp_642_code import remove_similar_row

class TestRemoveSimilarRow(unittest.TestCase):

    def test_typical_case(self):
        test_list = [[1, 2, 3], [2, 1, 3], [3, 2, 1]]
        self.assertEqual(remove_similar_row(test_list), {(1, 2, 3)})

    def test_empty_list(self):
        test_list = []
        self.assertEqual(remove_similar_row(test_list), set())

    def test_single_row(self):
        test_list = [[1, 2, 3]]
        self.assertEqual(remove_similar_row(test_list), {(1, 2, 3)})

    def test_duplicate_rows(self):
        test_list = [[1, 2, 3], [1, 2, 3]]
        self.assertEqual(remove_similar_row(test_list), {(1, 2, 3)})

    def test_large_input(self):
        test_list = [[1, 2, 3], [2, 1, 3], [3, 2, 1], [1, 2, 3], [3, 2, 1]]
        self.assertEqual(remove_similar_row(test_list), {(1, 2, 3), (3, 2, 1)})

    def test_mixed_types(self):
        test_list = [['1', 2, 3], [2, '1', 3], [3, 2, '1']]
        self.assertEqual(remove_similar_row(test_list), {(1, 2, 3)})
