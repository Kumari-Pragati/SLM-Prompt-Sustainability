import unittest
from mbpp_219_code import extract_min_max

class TestExtractMinMax(unittest.TestCase):

    def test_simple_inputs(self):
        self.assertEqual(extract_min_max((1, 2, 3, 4, 5), 2), (1, 5))
        self.assertEqual(extract_min_max((10, 20, 30, 40, 50), 3), (10, 50))

    def test_edge_conditions(self):
        self.assertEqual(extract_min_max((1, 2, 3, 4, 5), 0), ())
        self.assertEqual(extract_min_max((1, 2, 3, 4, 5), 5), (1, 2, 3, 4, 5))
        self.assertEqual(extract_min_max((1,), 1), (1,))

    def test_boundary_conditions(self):
        self.assertEqual(extract_min_max((1, 2, 3, 4, 5), 1), (1,))
        self.assertEqual(extract_min_max((1, 2, 3, 4, 5), 4), (1, 2, 3, 5))

    def test_complex_cases(self):
        self.assertEqual(extract_min_max((1, 2, 3, 4, 5, 6, 7, 8, 9), 3), (1, 9))
        self.assertEqual(extract_min_max((10, 20, 30, 40, 50, 60, 70, 80, 90), 4), (10, 90))
