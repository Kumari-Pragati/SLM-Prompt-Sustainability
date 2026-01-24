import unittest
from mbpp_110_code import extract_missing

class TestExtractMissing(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(extract_missing([[1, 2], [3, 4]], 0, 5), [(0, 2), (2, 4)])

    def test_empty_input(self):
        self.assertEqual(extract_missing([], 0, 5), [])

    def test_single_element(self):
        self.assertEqual(extract_missing([[1, 2]], 0, 5), [(0, 2)])

    def test_strt_val_equal_stop_val(self):
        self.assertEqual(extract_missing([[1, 2]], 2, 2), [])

    def test_stop_val_greater_than_max(self):
        self.assertEqual(extract_missing([[1, 2], [3, 4]], 0, 6), [(0, 2), (2, 4)])

    def test_stop_val_less_than_min(self):
        self.assertEqual(extract_missing([[1, 2], [3, 4]], 0, -1), [(0, 2)])

    def test_multiple_elements(self):
        self.assertEqual(extract_missing([[1, 2], [3, 4], [5, 6]], 0, 7), [(0, 2), (2, 4), (4, 6)])
