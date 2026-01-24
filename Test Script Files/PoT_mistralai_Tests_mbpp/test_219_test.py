import unittest
from mbpp_219_code import extract_min_max

class TestExtractMinMax(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(extract_min_max((1, 2, 3, 4, 5), 2), (1, 3))
        self.assertEqual(extract_min_max((-1, -2, -3, -4, -5), 2), (-1, -3))
        self.assertEqual(extract_min_max((0, 0, 0, 0, 0), 2), (0, 0))

    def test_edge_case_min_length(self):
        self.assertEqual(extract_min_max((1,), 2), (1,))
        self.assertEqual(extract_min_max((1, 2), 3), (1, 2))
        self.assertEqual(extract_min_max((1, 2, 3), 4), (1, 2, 3))
        self.assertEqual(extract_min_max((1, 2, 3, 4), 5), (1, 2, 3, 4))

    def test_edge_case_K_greater_than_length(self):
        self.assertEqual(extract_min_max((1, 2, 3), 4), (1, 2, 3))

    def test_edge_case_K_zero(self):
        self.assertEqual(extract_min_max((1, 2, 3), 0), tuple())
