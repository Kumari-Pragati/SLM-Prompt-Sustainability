import unittest
from mbpp_642_code import remove_similar_row

class TestRemoveSimilarRow(unittest.TestCase):
    def test_empty_input(self):
        self.assertEqual(remove_similar_row([]), set())

    def test_single_row(self):
        self.assertEqual(remove_similar_row([[]]), set())

    def test_multiple_rows(self):
        self.assertEqual(remove_similar_row([[1, 2, 3], [2, 3, 4], [3, 4, 5]]), {frozenset([1, 2, 3]), frozenset([2, 3, 4]), frozenset([3, 4, 5])})

    def test_duplicate_rows(self):
        self.assertEqual(remove_similar_row([[1, 2, 3], [2, 3, 4], [2, 3, 4]]), {frozenset([1, 2, 3]), frozenset([2, 3, 4])})

    def test_empty_row(self):
        self.assertEqual(remove_similar_row([[], [1, 2, 3], [2, 3, 4]]), {frozenset([1, 2, 3]), frozenset([2, 3, 4])})

    def test_row_with_duplicates(self):
        self.assertEqual(remove_similar_row([[1, 1, 2], [2, 2, 3], [2, 2, 3]]), {frozenset([1, 2]), frozenset([2, 3])})
