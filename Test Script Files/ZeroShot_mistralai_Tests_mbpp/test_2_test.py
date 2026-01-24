import unittest
from mbpp_2_code import similar_elements

class TestSimilarElements(unittest.TestCase):

    def test_empty_tuples(self):
        self.assertCountEqual(similar_elements((), ()), ())

    def test_single_element_tuples(self):
        self.assertCountEqual(similar_elements((1,), (1,)), (1,))
        self.assertCountEqual(similar_elements((1,), (2,)), ())

    def test_identical_tuples(self):
        self.assertCountEqual(similar_elements((1, 2, 3), (1, 2, 3)), (1, 2, 3))

    def test_overlapping_tuples(self):
        self.assertCountEqual(similar_elements((1, 2, 3, 4), (2, 3, 5, 6)), (2, 3))

    def test_non_overlapping_tuples(self):
        self.assertCountEqual(similar_elements((1, 2, 3, 4), (5, 6, 7, 8)), ())

    def test_different_order_tuples(self):
        self.assertCountEqual(similar_elements((1, 2, 3), (3, 1, 2)), (1, 2, 3))
