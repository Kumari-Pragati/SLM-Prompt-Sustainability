import unittest
from mbpp_219_code import extract_min_max

class TestExtractMinMax(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(extract_min_max((1, 2, 3, 4, 5), 2), (1, 5))
        self.assertEqual(extract_min_max((10, 20, 30, 40, 50), 3), (10, 30, 50))
        self.assertEqual(extract_min_max((100, 200, 300, 400, 500), 1), (100,))
        self.assertEqual(extract_min_max((1, 2, 3, 4, 5), 5), (1, 2, 3, 4, 5))

    def test_edge(self):
        self.assertEqual(extract_min_max((), 2), ())
        self.assertEqual(extract_min_max((1,), 1), (1,))
        self.assertEqual(extract_min_max((1, 2), 2), (1, 2))
        self.assertEqual(extract_min_max((1, 2, 3, 4, 5), 0), ())
        self.assertEqual(extract_min_max((1, 2, 3, 4, 5), 6), (1, 2, 3, 4, 5))

    def test_complex(self):
        self.assertEqual(extract_min_max((1, 2, 3, 4, 5, 6, 7, 8, 9, 10), 3), (1, 5, 10))
        self.assertEqual(extract_min_max((10, 20, 30, 40, 50, 60, 70, 80, 90, 100), 4), (10, 30, 60, 100))
        self.assertEqual(extract_min_max((1, 2, 3, 4, 5, 6, 7, 8, 9, 10), 10), (1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
