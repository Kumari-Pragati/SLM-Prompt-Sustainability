import unittest
from mbpp_2_code import similar_elements

class TestSimilarElements(unittest.TestCase):

    def test_similar_elements(self):
        self.assertEqual(similar_elements((1, 2, 3, 4), (3, 4, 5, 6)), (3, 4))
        self.assertEqual(similar_elements((1, 2, 3, 4), (4, 5, 6, 7)), (4,))
        self.assertEqual(similar_elements((1, 2, 3, 4), (1, 2, 3, 4)), (1, 2, 3, 4))
        self.assertEqual(similar_elements((1, 2, 3, 4), (5, 6, 7, 8)), ())
        self.assertEqual(similar_elements((), ()), ())
        self.assertEqual(similar_elements((1, 2, 3), (2, 3, 4)), (2, 3))
        self.assertEqual(similar_elements((1, 2, 3), (4, 5, 6)), ())

    def test_similar_elements_empty(self):
        self.assertEqual(similar_elements((), ()), ())
        self.assertEqual(similar_elements((1, 2, 3), ()), ())
