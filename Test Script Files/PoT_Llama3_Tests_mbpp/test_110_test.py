import unittest
from mbpp_110_code import extract_missing

class TestExtractMissing(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(extract_missing([(1, 2), (3, 4), (5, 6)], 1, 6), [(1, 2), (2, 3), (3, 4), (4, 5), (5, 6)])

    def test_edge_case_start(self):
        self.assertEqual(extract_missing([(1, 2), (3, 4), (5, 6)], 2, 6), [(2, 3), (3, 4), (4, 5), (5, 6)])

    def test_edge_case_stop(self):
        self.assertEqual(extract_missing([(1, 2), (3, 4), (5, 6)], 1, 5), [(1, 2), (2, 3), (3, 4), (4, 5)])

    def test_edge_case_start_stop(self):
        self.assertEqual(extract_missing([(1, 2), (3, 4), (5, 6)], 2, 5), [(2, 3), (3, 4), (4, 5)])

    def test_empty_input(self):
        self.assertEqual(extract_missing([], 1, 6), [])

    def test_single_input(self):
        self.assertEqual(extract_missing([(1, 2)], 1, 6), [(1, 2)])

    def test_invalid_input_type(self):
        with self.assertRaises(TypeError):
            extract_missing('test', 1, 6)

    def test_invalid_input_value(self):
        with self.assertRaises(ValueError):
            extract_missing([(1, 'test')], 1, 6)
