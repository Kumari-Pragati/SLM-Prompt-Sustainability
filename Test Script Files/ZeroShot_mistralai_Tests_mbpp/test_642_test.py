import unittest
from mbpp_642_code import remove_similar_row

class TestRemoveSimilarRow(unittest.TestCase):

    def test_empty_list(self):
        self.assertListEqual(remove_similar_row([]), [])

    def test_single_element(self):
        self.assertListEqual(remove_similar_row([[1, 2, 3]]), [[1, 2, 3]])

    def test_duplicates(self):
        self.assertListEqual(remove_similar_row([[1, 2, 3], [1, 2, 3]]), [[1, 2, 3]])

    def test_no_duplicates(self):
        self.assertListEqual(remove_similar_row([[1, 2, 3], [4, 5, 6]]), [[1, 2, 3], [4, 5, 6]])

    def test_mixed_duplicates(self):
        self.assertListEqual(remove_similar_row([[1, 2, 3], [1, 2, 3], [4, 5, 6]]), [[1, 2, 3], [4, 5, 6]])

    def test_sorted_list(self):
        self.assertListEqual(remove_similar_row([[3, 2, 1], [1, 2, 3]]), [[1, 2, 3]])

    def test_unsorted_list(self):
        self.assertListEqual(remove_similar_row([[1, 2, 3], [3, 2, 1]]), [[1, 2, 3]])

    def test_nested_lists(self):
        self.assertListEqual(remove_similar_row([[[1, 2, 3]], [[1, 2, 3]]]), [[[1, 2, 3]]])
