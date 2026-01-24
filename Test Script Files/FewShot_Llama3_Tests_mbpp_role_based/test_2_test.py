import unittest
from mbpp_2_code import similar_elements

class TestSimilarElements(unittest.TestCase):
    def test_empty_tuples(self):
        self.assertEqual(similar_elements((), ()), ())

    def test_no_common_elements(self):
        self.assertEqual(similar_elements((1, 2, 3), (4, 5, 6)), ())

    def test_common_elements(self):
        self.assertEqual(similar_elements((1, 2, 3), (2, 3, 4)), (2, 3))

    def test_duplicates(self):
        self.assertEqual(similar_elements((1, 2, 2, 3), (2, 3, 3, 4)), (2, 3))

    def test_order_matters(self):
        self.assertEqual(similar_elements((1, 2, 3), (3, 2, 1)), (1, 2, 3))

    def test_order_doesnt_matter(self):
        self.assertEqual(similar_elements((1, 2, 3), (1, 2, 3)), (1, 2, 3))
