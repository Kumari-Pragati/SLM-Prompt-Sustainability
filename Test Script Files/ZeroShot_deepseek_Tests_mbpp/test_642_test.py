import unittest
from mbpp_642_code import remove_similar_row

class TestRemoveSimilarRow(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(remove_similar_row([]), set())

    def test_single_element(self):
        self.assertEqual(remove_similar_row([[1]]), {tuple([1])} )

    def test_multiple_elements(self):
        self.assertEqual(remove_similar_row([[1, 2], [2, 1]]), {tuple([1, 2])} )

    def test_duplicate_elements(self):
        self.assertEqual(remove_similar_row([[1, 1], [2, 2]]), {tuple([1]), tuple([2])} )

    def test_mixed_elements(self):
        self.assertEqual(remove_similar_row([[1, 2, 3], [3, 2, 1], [1, 1, 1]]), {tuple([1, 2, 3]), tuple([1])} )
