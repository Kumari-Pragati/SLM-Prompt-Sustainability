import unittest
from mbpp_219_code import extract_min_max

class TestExtractMinMax(unittest.TestCase):

    def test_extract_min_max(self):
        self.assertEqual(extract_min_max((1, 2, 3, 4, 5), 2), (1, 2, 4, 5))
        self.assertEqual(extract_min_max((1, 2, 3, 4, 5), 3), (1, 2, 3, 4, 5))
        self.assertEqual(extract_min_max((1, 2, 3, 4, 5), 1), (1, 5))
        self.assertEqual(extract_min_max((1, 2, 3, 4, 5), 5), (1, 2, 3, 4, 5))
        self.assertEqual(extract_min_max((1, 2, 3, 4, 5), 0), (1, 5))
        self.assertEqual(extract_min_max((1, 2, 3, 4, 5), 6), (1, 2, 3, 4, 5))

    def test_extract_min_max_edge_cases(self):
        self.assertEqual(extract_min_max((1, 2), 1), (1, 2))
        self.assertEqual(extract_min_max((1, 2), 0), (1, 2))
        self.assertEqual(extract_min_max((1, 2), 3), (1, 2))
