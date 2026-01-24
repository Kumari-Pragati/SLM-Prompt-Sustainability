import unittest
from mbpp_642_code import remove_similar_row

class TestRemoveSimilarRow(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(remove_similar_row([]), set())

    def test_single_row(self):
        self.assertEqual(remove_similar_row([[1, 2, 3]]), {(1, 2, 3)})

    def test_multiple_rows(self):
        self.assertEqual(remove_similar_row([[1, 2, 3], [3, 2, 1], [1, 2, 3]]), {(1, 2, 3)})

    def test_duplicates(self):
        self.assertEqual(remove_similar_row([[1, 2, 3], [1, 2, 3], [1, 2, 3]]), {(1, 2, 3)})

    def test_empty_row(self):
        self.assertEqual(remove_similar_row([[], [1, 2, 3]]), {(1, 2, 3)})

    def test_empty_row_with_duplicates(self):
        self.assertEqual(remove_similar_row([[], [1, 2, 3], [1, 2, 3]]), {(1, 2, 3)})

    def test_empty_row_with_duplicates_and_empty(self):
        self.assertEqual(remove_similar_row([[], [1, 2, 3], [1, 2, 3], []]), {(1, 2, 3)})
