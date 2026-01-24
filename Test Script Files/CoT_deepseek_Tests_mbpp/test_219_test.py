import unittest
from mbpp_219_code import extract_min_max

class TestExtractMinMax(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(extract_min_max((1, 2, 3, 4, 5), 2), (1, 5))

    def test_single_element(self):
        self.assertEqual(extract_min_max((5), 1), (5,))

    def test_large_k(self):
        self.assertEqual(extract_min_max((1, 2, 3, 4, 5), 5), (1, 5))

    def test_small_k(self):
        self.assertEqual(extract_min_max((1, 2, 3, 4, 5), 0), ())

    def test_negative_k(self):
        with self.assertRaises(ValueError):
            extract_min_max((1, 2, 3, 4, 5), -1)

    def test_k_greater_than_length(self):
        with self.assertRaises(ValueError):
            extract_min_max((1, 2, 3, 4, 5), 6)

    def test_empty_tuple(self):
        self.assertEqual(extract_min_max((), 1), ())

    def test_duplicate_values(self):
        self.assertEqual(extract_min_max((1, 2, 2, 3, 4, 5), 2), (1, 5))

    def test_sorted_tuple(self):
        self.assertEqual(extract_min_max((1, 2, 3, 4, 5), 2), (1, 5))

    def test_unsorted_tuple(self):
        self.assertEqual(extract_min_max((5, 1, 2, 3, 4), 2), (1, 5))
