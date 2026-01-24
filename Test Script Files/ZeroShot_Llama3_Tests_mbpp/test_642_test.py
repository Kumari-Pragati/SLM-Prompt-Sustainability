import unittest
from mbpp_642_code import remove_similar_row

class TestRemoveSimilarRow(unittest.TestCase):

    def test_remove_similar_row(self):
        self.assertEqual(remove_similar_row([[1, 2, 3], [1, 2, 3], [4, 5, 6]]), {[(1, 2, 3), (4, 5, 6)]})
        self.assertEqual(remove_similar_row([[1, 2, 3], [4, 5, 6], [1, 2, 3]]), {[(1, 2, 3), (4, 5, 6)]})
        self.assertEqual(remove_similar_row([[1, 2, 3], [1, 2, 3], [4, 5, 6]]), {[(1, 2, 3), (4, 5, 6)]})
        self.assertEqual(remove_similar_row([[1, 2, 3], [4, 5, 6], [1, 2, 3], [4, 5, 6]]), {[(1, 2, 3), (4, 5, 6)]})
        self.assertEqual(remove_similar_row([[1, 2, 3], [1, 2, 3], [1, 2, 3], [4, 5, 6]]), {[(1, 2, 3), (4, 5, 6)]})
        self.assertEqual(remove_similar_row([[1, 2, 3], [1, 2, 3], [1, 2, 3], [1, 2, 3]]), {[(1, 2, 3)]})
        self.assertEqual(remove_similar_row([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), {[(1, 2, 3), (4, 5, 6), (7, 8, 9)]})
        self.assertEqual(remove_similar_row([[1, 2, 3], [1, 2, 3], [4, 5, 6], [7, 8, 9]]), {[(1, 2, 3), (4, 5, 6), (7, 8, 9)]})
        self.assertEqual(remove_similar_row([[1, 2, 3], [1, 2, 3], [1, 2, 3], [4, 5, 6], [7, 8, 9]]), {[(1, 2, 3), (4, 5, 6), (7, 8, 9)]})
        self.assertEqual(remove_similar_row([[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 2, 3]]), {[(1, 2, 3), (4, 5, 6), (7, 8, 9)]})
        self.assertEqual(remove_similar_row([[1, 2, 3], [1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 2, 3]]), {[(1, 2, 3), (4, 5, 6), (7, 8, 9)]})
        self.assertEqual(remove_similar_row([[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 2, 3], [4, 5, 6]]), {[(1, 2, 3), (4, 5, 6), (7, 8, 9)]})
        self.assertEqual(remove_similar_row([[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 2, 3], [4, 5, 6], [7, 8, 9]]), {[(1, 2, 3), (4, 5, 6), (7, 8, 9)]})
