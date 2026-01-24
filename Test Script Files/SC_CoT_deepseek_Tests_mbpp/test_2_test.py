import unittest
from mbpp_2_code import similar_elements

class TestSimilarElements(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(similar_elements((1, 2, 3), (3, 4, 5)), (3,))

    def test_empty_tuples(self):
        self.assertEqual(similar_elements((), ()), ())

    def test_single_element(self):
        self.assertEqual(similar_elements((1,), (1,)), (1,))

    def test_no_similar_elements(self):
        self.assertEqual(similar_elements((1, 2, 3), (4, 5, 6)), ())

    def test_duplicate_elements(self):
        self.assertEqual(similar_elements((1, 2, 2), (2, 3, 3)), (2,))

    def test_unordered_tuples(self):
        self.assertEqual(similar_elements((3, 1, 2), (2, 3, 1)), (1, 2, 3))

    def test_large_tuples(self):
        large_tuple = tuple(range(1, 10001))
        self.assertEqual(similar_elements(large_tuple, large_tuple), large_tuple)
