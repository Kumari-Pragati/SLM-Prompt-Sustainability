import unittest
from mbpp_2_code import similar_elements

class TestSimilarElements(unittest.TestCase):
    def test_empty_tuples(self):
        self.assertEqual(similar_elements((), ()), ())

    def test_singletons(self):
        self.assertEqual(similar_elements((1,), (1,)), (1,))
        self.assertEqual(similar_elements((1,), ()), ())
        self.assertEqual(similar_elements((), (1,)), ())

    def test_common_elements(self):
        self.assertEqual(similar_elements((1, 2, 3), (2, 3, 4)), (2, 3))
        self.assertEqual(similar_elements((1, 2, 3), (3, 4, 5)), (3,))
        self.assertEqual(similar_elements((1, 2, 3), (1, 2, 3)), (1, 2, 3))

    def test_disjoint_sets(self):
        self.assertEqual(similar_elements((1, 2, 3), (4, 5, 6)), ())
        self.assertEqual(similar_elements((1, 2, 3), (7, 8, 9)), ())

    def test_duplicates(self):
        self.assertEqual(similar_elements((1, 1, 2), (1, 2, 2)), (1, 2))
