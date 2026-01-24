import unittest
from mbpp_110_code import extract_missing

class TestExtractMissing(unittest.TestCase):

    def test_empty_list(self):
        self.assertListEqual(extract_missing([], 1, 3), [])

    def test_single_element(self):
        self.assertListEqual(extract_missing([(2, 3)], 1, 3), [(1, 2)])

    def test_multiple_elements(self):
        self.assertListEqual(extract_missing([(1, 2), (3, 4), (5, 6)], 1, 6), [(1, 1), (1, 2), (3, 3), (5, 5), (6, 6)])

    def test_start_value_in_list(self):
        self.assertListEqual(extract_missing([(2, 3), (4, 5)], 2, 5), [(2, 2), (4, 4)])

    def test_stop_value_in_list(self):
        self.assertListEqual(extract_missing([(1, 2), (3, 4)], 1, 4), [(1, 1)])
