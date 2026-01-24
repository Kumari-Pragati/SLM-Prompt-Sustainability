import unittest
from mbpp_2_code import similar_elements

class TestSimilarElements(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(similar_elements((1, 2, 3), (3, 4, 5)), (3,))

    def test_empty_tuples(self):
        self.assertEqual(similar_elements((), ()), ())

    def test_same_elements(self):
        self.assertEqual(similar_elements((1, 2, 2, 3), (2, 2, 3, 4)), (2, 3))

    def test_no_similar_elements(self):
        self.assertEqual(similar_elements((1, 2, 3), (4, 5, 6)), ())

    def test_duplicate_elements(self):
        self.assertEqual(similar_elements((1, 1, 2, 3), (1, 2, 2, 3)), (1, 2, 3))

    def test_one_empty_tuple(self):
        self.assertEqual(similar_elements((1, 2, 3), ()), ())

    def test_negative_numbers(self):
        self.assertEqual(similar_elements((-1, -2, -3), (-3, -4, -5)), (-3,))

    def test_mixed_types(self):
        self.assertEqual(similar_elements((1, 'a', 3), (3, 'b', 1)), (1, 3))

    def test_large_tuples(self):
        large_tuple = tuple(range(1, 1001))
        self.assertEqual(similar_elements(large_tuple, large_tuple), large_tuple)
