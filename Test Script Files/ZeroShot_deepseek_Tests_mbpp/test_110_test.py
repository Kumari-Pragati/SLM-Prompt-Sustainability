import unittest
from mbpp_110_code import extract_missing

class TestExtractMissing(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(extract_missing([], 1, 10), [])

    def test_single_value(self):
        self.assertEqual(extract_missing([(2, 5)], 1, 10), [(1, 2), (5, 10)])

    def test_multiple_values(self):
        self.assertEqual(extract_missing([(2, 5), (7, 9)], 1, 10), [(1, 2), (5, 7), (9, 10)])

    def test_start_and_stop_values(self):
        self.assertEqual(extract_missing([(2, 5)], 2, 5), [])

    def test_start_value_greater_than_stop_value(self):
        self.assertEqual(extract_missing([(2, 5)], 5, 2), [])

    def test_start_and_stop_values_not_in_list(self):
        self.assertEqual(extract_missing([(2, 5), (7, 9)], 3, 6), [(3, 3), (6, 3)])
