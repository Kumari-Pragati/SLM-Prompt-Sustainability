import unittest
from mbpp_219_code import extract_min_max

class TestExtractMinMax(unittest.TestCase):

    def test_empty_list(self):
        self.assertIsInstance(extract_min_max((), 0), tuple)
        self.assertIsNone(extract_min_max((), 1))

    def test_single_element(self):
        self.assertEqual(extract_min_max((1,), 0), (1,))
        self.assertEqual(extract_min_max((1,), 1), (1,))

    def test_small_list(self):
        self.assertEqual(extract_min_max((1, 2, 3, 4), 2), (2, 3, 4))
        self.assertEqual(extract_min_max((1, 2, 3, 4), 1), (1, 2, 3))

    def test_large_list(self):
        test_tup = tuple(range(100))
        self.assertEqual(extract_min_max(test_tup, 50), sorted(test_tup)[25:75])
