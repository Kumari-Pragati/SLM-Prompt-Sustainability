import unittest
from mbpp_110_code import extract_missing

class TestExtractMissing(unittest.TestCase):

    def test_empty_list(self):
        self.assertListEqual(extract_missing([], 1, 3), [])

    def test_single_element(self):
        self.assertListEqual(extract_missing([(2, 3)], 1, 3), [(1, 2)])

    def test_multiple_elements(self):
        self.assertListEqual(extract_missing([(1, 2), (3, 4), (5, 6)], 0, 7), [(0, 1), (3, 4)])

    def test_start_equal_stop(self):
        self.assertListEqual(extract_missing([(1, 1)], 1, 1), [])

    def test_start_greater_stop(self):
        self.assertListEqual(extract_missing([(2, 1)], 1, 2), [(1, 2)])

    def test_start_less_stop_less_first_element(self):
        self.assertListEqual(extract_missing([(3, 4)], 1, 2), [(1, 3)])

    def test_start_less_stop_greater_first_element(self):
        self.assertListEqual(extract_missing([(1, 4)], 1, 3), [(1, 1), (3, 4)])

    def test_start_less_equal_first_element_stop_greater_last_element(self):
        self.assertListEqual(extract_missing([(1, 4), (5, 6)], 1, 5), [(1, 1), (5, 5)])

    def test_start_greater_first_element_stop_less_last_element(self):
        self.assertListEqual(extract_missing([(2, 4), (5, 6)], 1, 3), [(1, 2)])

    def test_start_equal_first_element_stop_equal_last_element(self):
        self.assertListEqual(extract_missing([(1, 1), (2, 2)], 1, 2), [(1, 1)])

    def test_start_equal_first_element_stop_greater_last_element(self):
        self.assertListEqual(extract_missing([(1, 1), (2, 2)], 1, 3), [(1, 1)])

    def test_start_greater_first_element_stop_equal_last_element(self):
        self.assertListEqual(extract_missing([(2, 2), (1, 1)], 1, 2), [(1, 2)])

    def test_start_less_first_element_stop_less_last_element(self):
        self.assertListEqual(extract_missing([(3, 4), (1, 2)], 1, 3), [(1, 3)])

    def test_start_less_first_element_stop_greater_last_element(self):
        self.assertListEqual(extract_missing([(3, 4), (1, 2)], 1, 5), [(1, 3), (5, 5)])

    def test_start_greater_first_element_stop_less_last_element_empty_list(self):
        self.assertListEqual(extract_missing([], 3, 2), [])

    def test_start_greater_first_element_stop_less_last_element_single_element(self):
        self.assertListEqual(extract_missing([(1, 2)], 3, 2), [(3, 2)])

    def test_start_greater_first_element_stop_less_last_element_multiple_elements(self):
        self.assertListEqual(extract_missing([(1, 2), (3, 4), (5, 6)], 3, 2), [(3, 3)])

if __name