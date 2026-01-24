import unittest
from mbpp_110_code import extract_missing

class TestExtractMissing(unittest.TestCase):
    def test_typical(self):
        self.assertEqual(extract_missing([(1, 2), (3, 4), (5, 6)], 0, 10), [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 6)])

    def test_edge_start(self):
        self.assertEqual(extract_missing([(1, 2), (3, 4), (5, 6)], 1, 10), [(1, 2), (2, 3), (3, 4), (4, 5), (5, 6)])

    def test_edge_stop(self):
        self.assertEqual(extract_missing([(1, 2), (3, 4), (5, 6)], 0, 5), [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5)])

    def test_edge_start_stop(self):
        self.assertEqual(extract_missing([(1, 2), (3, 4), (5, 6)], 2, 4), [(2, 3), (3, 4)])

    def test_empty_input(self):
        self.assertEqual(extract_missing([], 0, 10), [])

    def test_single_input(self):
        self.assertEqual(extract_missing([(1, 2)], 0, 10), [(0, 1)])

    def test_invalid_input_type(self):
        with self.assertRaises(TypeError):
            extract_missing('test', 0, 10)

    def test_invalid_input_value(self):
        with self.assertRaises(TypeError):
            extract_missing([(1, 2)], '0', 10)
