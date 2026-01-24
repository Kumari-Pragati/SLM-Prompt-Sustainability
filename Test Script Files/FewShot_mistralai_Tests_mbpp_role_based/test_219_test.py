import unittest
from mbpp_219_code import extract_min_max

class TestExtractMinMax(unittest.TestCase):
    def test_valid_input_length(self):
        self.assertEqual(extract_min_max((1, 2, 3, 4, 5), 2), (1, 3))
        self.assertEqual(extract_min_max((1, 2, 3, 4, 5), 3), (1, 2, 4))
        self.assertEqual(extract_min_max((1, 2, 3, 4, 5), 4), (1, 2, 3, 4))
        self.assertEqual(extract_min_max((1, 2, 3, 4, 5), 5), (1, 2, 3, 4, 5))

    def test_empty_input(self):
        self.assertEqual(extract_min_max((), 2), (None, None))

    def test_single_input(self):
        self.assertEqual(extract_min_max((1,), 1), (1,))

    def test_negative_index(self):
        with self.assertRaises(IndexError):
            extract_min_max((1, 2, 3, 4, 5), -1)

    def test_invalid_K(self):
        with self.assertRaises(ValueError):
            extract_min_max((1, 2, 3, 4, 5), 6)
