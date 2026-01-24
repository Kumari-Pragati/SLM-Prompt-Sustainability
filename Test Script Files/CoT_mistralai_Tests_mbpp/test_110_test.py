import unittest
from mbpp_110_code import extract_missing

class TestExtractMissing(unittest.TestCase):
    def test_empty_list(self):
        self.assertListEqual(extract_missing([], 1, 3), [])

    def test_single_element(self):
        self.assertListEqual(extract_missing([(2, 3)], 1, 3), [(1, 2)])

    def test_multiple_elements(self):
        self.assertListEqual(extract_missing([(1, 2), (3, 4), (5, 6)], 0, 7), [(0, 1), (3, 4)])

    def test_start_equal_to_first_element(self):
        self.assertListEqual(extract_missing([(1, 2)], 1, 2), [(1, 2)])

    def test_stop_equal_to_last_element(self):
        self.assertListEqual(extract_missing([(1, 2), (3, 4)], 1, 4), [(1, 2), (3, 4)])

    def test_start_greater_than_last_element(self):
        self.assertListEqual(extract_missing([(1, 2), (3, 4)], 5, 4), [(5, 1)])

    def test_stop_less_than_start(self):
        self.assertListEqual(extract_missing([(1, 2), (3, 4)], 1, 0), [])

    def test_invalid_start(self):
        with self.assertRaises(ValueError):
            extract_missing([(1, 2)], -1, 1)

    def test_invalid_stop(self):
        with self.assertRaises(ValueError):
            extract_missing([(1, 2)], 1, 0)
