import unittest
from mbpp_110_code import extract_missing

class TestExtractMissing(unittest.TestCase):

    def test_simple_input(self):
        self.assertEqual(extract_missing([(1, 3), (4, 6), (7, 9)], 1, 9), [(1, 3), (4, 6), (7, 9)])

    def test_edge_condition_start_value_greater_than_stop_value(self):
        self.assertEqual(extract_missing([(3, 1)], 1, 3), [])

    def test_edge_condition_start_value_equal_to_stop_value(self):
        self.assertEqual(extract_missing([(1, 1)], 1, 2), [])

    def test_edge_condition_empty_input(self):
        self.assertEqual(extract_missing([], 1, 3), [])

    def test_complex_input(self):
        self.assertEqual(extract_missing([(1, 3), (5, 7), (9, 11)], 1, 11), [(1, 3), (5, 7), (9, 11)])

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            extract_missing([(1, 'a')], 1, 3)
