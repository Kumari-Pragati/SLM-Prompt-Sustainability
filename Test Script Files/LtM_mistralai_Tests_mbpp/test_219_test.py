import unittest
from mbpp_219_code import extract_min_max

class TestExtractMinMax(unittest.TestCase):

    def test_simple(self):
        self.assertEqual(extract_min_max((1, 2, 3, 4, 5), 2), (1, 3))
        self.assertEqual(extract_min_max((-1, -2, -3, -4, -5), 2), (-1, -3))
        self.assertEqual(extract_min_max((0, 0, 0, 0, 0), 2), (0, 0))

    def test_edge_and_boundary(self):
        self.assertEqual(extract_min_max((1, 2, 3, 4, 5), 1), (1,))
        self.assertEqual(extract_min_max((1, 2, 3, 4, 5), 3), (3, 5))
        self.assertEqual(extract_min_max((1, 2, 3, 4, 5), 0), ())
        self.assertEqual(extract_min_max((1, 2, 3, 4, 5), 4), ())
        self.assertEqual(extract_min_max((1, 2, 3, 4, 5), 5), (1, 2, 3, 4, 5))

    def test_complex(self):
        self.assertEqual(extract_min_max((float('inf'), 2, 3, float('-inf')), 2), (2, 3))
        self.assertEqual(extract_min_max((-float('inf'), 2, 3, float('inf')), 2), (2, 3))
        self.assertEqual(extract_min_max((-float('inf'), 2, 3, float('inf')), 1), (2,))
        self.assertEqual(extract_min_max((-float('inf'), 2, 3, float('inf')), 3), (3, float('inf')))
